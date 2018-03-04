"""
    Copyright (C) 2017, ContraxSuite, LLC

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    You can also be released from the requirements of the license by purchasing
    a commercial license from ContraxSuite, LLC. Buying such a license is
    mandatory as soon as you develop commercial activities involving ContraxSuite
    software without disclosing the source code of your own applications.  These
    activities include: offering paid services to customers as an ASP or "cloud"
    provider, processing documents on the fly in a web application,
    or shipping ContraxSuite within a closed source product.
"""

from typing import Dict, Tuple, List

from lexnlp.nlp.en.segments.sentences import get_sentence_span_list

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2018, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-contraxsuite/blob/1.0.5/LICENSE"
__version__ = "1.0.7"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class SkLearnClassifierModel:
    EMPTY_CAT_NAME = '-'

    def __init__(self, sklearn_model, target_names) -> None:
        self.sklearn_model = sklearn_model
        self.target_names = target_names

    def detect_category_names_to_spans(self, text: str, field: str = None) \
            -> Dict[str, List[Tuple[int, int, str]]]:
        if self.sklearn_model is None:
            return {}

        sentence_spans = get_sentence_span_list(text)

        res = {}

        for span in sentence_spans:
            sentence = text[span[0]:span[1]]
            predicted = self.sklearn_model.predict([sentence]).toarray()[0]

            for target_index, value in enumerate(predicted):
                if not value:
                    continue
                target_name = self.target_names[target_index]
                if target_name == SkLearnClassifierModel.EMPTY_CAT_NAME:
                    continue

                if (not field and target_name) or (field and field == target_name):
                    spans_of_category = res.get(target_name)
                    if not spans_of_category:
                        spans_of_category = [(span[0], span[1], sentence)]
                        res[target_name] = spans_of_category
                    else:
                        spans_of_category.append((span[0], span[1], sentence))
        return res