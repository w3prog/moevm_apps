$(document).ready(function () {
    var filterFunction = function (container, filterValues, getItemValuesFunc) {
        $(container).each(function (index, item) {
            var itemValues = getItemValuesFunc(item);
            var valuesCount = filterValues.length;
            var shouldAppear = true;

            for (var i = 0; i < valuesCount; ++i) {
                if (filterValues[i] === '' || filterValues[i] === undefined) {
                    continue;
                }
                if (filterValues[i] !== itemValues[i]) {
                    shouldAppear = false;
                    break;
                }
            }

            if (shouldAppear) {
                $(item).show();
            } else {
                $(item).hide();
            }
        });
    };

    var studentsFilter = function () {
        var filterbox = $('#filter-box');

        var filterValues = [
            filterbox.find('#first-name').val(),
            filterbox.find('#last-name').val(),
            filterbox.find('#patronymic').val(),
            filterbox.find('#group').val(),
            filterbox.find('#e-mail').val(),
            filterbox.find('#github').val(),
            filterbox.find('#stepic').val()
        ];

        var getItemValues = function (item) {
            var $item = $(item);
            return [
                $item.find('span[js-key="first_name"]').attr('js-value'),
                $item.find('span[js-key="last_name"]').attr('js-value'),
                $item.find('span[js-key="patronymic"]').attr('js-value'),
                $item.find('span[js-key="study_group"]').attr('js-value'),
                $item.find('span[js-key="email"]').attr('js-value'),
                $item.find('span[js-key="github"]').attr('js-value'),
                $item.find('span[js-key="stepic"]').attr('js-value')
            ];
        };

        filterFunction('.student-block', filterValues, getItemValues);
    };

    var attendanceFilter = function () {
        var filterbox = $('#filter-box');

        var filterValues = [
            filterbox.find('#group').val()
        ];

        var getItemValues = function (item) {
            var $item = $(item);
            return [
                $item.find('h3[js-key="study_group"]').attr('js-value')
            ];
        };

        filterFunction('.attendance-table', filterValues, getItemValues);
    };

    var gradesFilter = function () {
        var filterbox = $('#filter-box');

        var filterValues = [
            filterbox.find('#group').val()
        ];

        var getItemValues = function (item) {
            var $item = $(item);
            return [
                $item.find('h3[js-key="study_group"]').attr('js-value')
            ];
        };

        console.log('yay');

        filterFunction('.grades-table', filterValues, getItemValues);
    };

    var timetableFilter = function () {
        var filterbox = $('#filter-box');

        var filterValues = [
            filterbox.find('#group').val()
        ];

        var getItemValues = function (item) {
            var $item = $(item);
            return [
                $item.find('caption[js-key="study_group"]').attr('js-value')
            ];
        };

        filterFunction('.timetable-table', filterValues, getItemValues);
    };

    var grouplistfilter = function () {
        var filterbox = $('#filter-box');

        var filterValues = [
            filterbox.find('#group').val()
        ];

        var getItemValues = function (item) {
            var $item = $(item);
            return [
                $item.find('caption[js-key="study_group"]').attr('js-value')
            ];
        };

        filterFunction('.grouplist-table', filterValues, getItemValues);
    };

    var termprojectsfilter = function () {
        var filterbox = $('#filter-box');

        var filterValues = [
            filterbox.find('#group').val()
        ];

        var getItemValues = function (item) {
            var $item = $(item);
            return [
                $item.find('caption[js-key="study_group"]').attr('js-value')
            ];
        };

        filterFunction('.termprojects-table', filterValues, getItemValues);
    };

    $('#apply-students-filter').on('click', studentsFilter);
    $('#apply-attendance-filter').on('click', attendanceFilter);
    $('#apply-grades-filter').on('click', gradesFilter);
    $('#apply-timetable-filter').on('click', timetableFilter);
    $('#apply-grouplist-filter').on('click', grouplistfilter);
    $('#apply-termprojects-filter').on('click', termprojectsfilter);
});