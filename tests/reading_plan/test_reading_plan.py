from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from tests.reading_plan.mock_reading_plan import RESULT_MOCK, RESULT_MOCK_2
import pytest
from unittest.mock import Mock, patch
from tests.reading_plan.mock_find_news import MOCK_FIND_NEWS


def test_reading_plan_group_news():
    FILE_MOCK = ('tech_news.analyzer.reading_plan.ReadingPlanService'
                 '._db_news_proxy')
    with pytest.raises(ValueError,
                       match="Valor 'available_time' deve ser maior que zero"):
        ReadingPlanService.group_news_for_available_time(0)

    mock_find_news = Mock(return_value=MOCK_FIND_NEWS)
    with patch(FILE_MOCK, mock_find_news):
        result = ReadingPlanService.group_news_for_available_time(18)

        assert result['unreadable'] == RESULT_MOCK['unreadable']
        assert RESULT_MOCK['readable'][0] in result['readable']
        assert len(result['readable']) == 22
        assert len(result['unreadable']) == 0

    mock_find_news = Mock(return_value=MOCK_FIND_NEWS)
    with patch(FILE_MOCK, mock_find_news):
        result = ReadingPlanService.group_news_for_available_time(4)
        assert len(result['readable']) == 1
        assert len(result['unreadable']) == 29
        assert result['unreadable'] == RESULT_MOCK_2['unreadable']
        assert RESULT_MOCK_2['readable'][0] in result['readable']
