/* Highcharts for dashboard coins -- on load */

$(document).ready(function(){
// begin chart for btc
    $('#btc_chart').highcharts({
        chart: {
            zoomType: 'x',
           // type: 'line'
        },
        credits: {
            enabled: false
        },
        xAxis: {

            lineWidth: 0,
            minorGridLineWidth: 0,
            lineColor: 'transparent',
            labels: {
                enabled: false
            },
            minorTickLength: 0,
            tickLength: 0,
            type: 'datetime',
            gridLineWidth: 0,
            title: {
                text: null
                },
        },
        title: {
            text: false
        },
        yAxis: {
            labels: {
                enabled: false
            },
            title: {
                text: null
                },
            gridLineWidth: 0
        },
        tooltip: {
            valueDecimals: 2,
            valuePrefix: '$',
            seriesName: ''
            //valueSuffix: ' USD'
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            },
            series: {
                tooltip: {
                    pointFormat: '<b>{point.y}</b><br/>'
                }
            }
        },
        series: [{
            type: 'area',
            showInLegend: false,
            data: {{btc_data | safe}}
        }]
    });

// begin chart for eth
    $('#eth_chart').highcharts({
        chart: {
            zoomType: 'x',
           // type: 'line'
        },
        credits: {
            enabled: false
        },
        xAxis: {

            lineWidth: 0,
            minorGridLineWidth: 0,
            lineColor: 'transparent',
            labels: {
                enabled: false
            },
            minorTickLength: 0,
            tickLength: 0,
            type: 'datetime',
            gridLineWidth: 0,
            title: {
                text: null
                },
        },
        title: {
            text: false
        },
        yAxis: {
            labels: {
                enabled: false
            },
            title: {
                text: null
                },
            gridLineWidth: 0
        },
        tooltip: {
            valueDecimals: 2,
            valuePrefix: '$',
            seriesName: ''
            //valueSuffix: ' USD'
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            },
            series: {
                tooltip: {
                    pointFormat: '<b>{point.y}</b><br/>'
                }
            }
        },
        series: [{
            type: 'area',
            showInLegend: false,
            data: {{eth_data | safe}}
        }]
    });

// begin chart for ltc
    $('#ltc_chart').highcharts({
        chart: {
            zoomType: 'x',
           // type: 'line'
        },
        credits: {
            enabled: false
        },
        xAxis: {

            lineWidth: 0,
            minorGridLineWidth: 0,
            lineColor: 'transparent',
            labels: {
                enabled: false
            },
            minorTickLength: 0,
            tickLength: 0,
            type: 'datetime',
            gridLineWidth: 0,
            title: {
                text: null
                },
        },
        title: {
            text: false
        },
        yAxis: {
            labels: {
                enabled: false
            },
            title: {
                text: null
                },
            gridLineWidth: 0
        },
        tooltip: {
            valueDecimals: 2,
            valuePrefix: '$',
            seriesName: ''
            //valueSuffix: ' USD'
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            },
            series: {
                tooltip: {
                    pointFormat: '<b>{point.y}</b><br/>'
                }
            }
        },
        series: [{
            type: 'area',
            showInLegend: false,
            data: {{ltc_data | safe}}
        }]
    });
});
