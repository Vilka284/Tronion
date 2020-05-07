var ctx = document.getElementById('currentResultChart').getContext('2d');
var last_two_min_chart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Red', 'Green', 'Yellow'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3],
            backgroundColor: [
                'red',
                'green',
                'yellow',
            ],
            borderColor: [
                'red',
                'green',
                'yellow',
            ],
            borderWidth: 0
        }]
    },
    options: {

    }
});
var timeline = document.getElementById('timeLineChart').getContext('2d');
var time_line_chart = new Chart(timeline, {
    type: 'line',
    data: {
        labels: ['Red', 'Green', 'Yellow', 'Blue'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 100],
            backgroundColor: [
                'red',
                'green',
                'yellow',
                'blue'
            ],
            borderColor: [
                'red',
                'green',
                'yellow',
            ],
            borderWidth: 0
        }]
    },
    options: {

    }
});