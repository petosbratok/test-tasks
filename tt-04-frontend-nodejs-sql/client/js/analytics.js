const getTool = async (id) => {
  fetch(`https://biotech-task.herokuapp.com/tools/get/${id}`,
        {
            method: "GET",
        }
    ).then(response => response.json())
    .then(data => {
        result = data.results[0]

        $('.tool-info').append( `
              <img class="tool-image" src="${result.pic}" alt="">
              <div class="info-panel">
                <div class="info-main">
                  <p class="title">${result.title}</p>
                  <div class="state-block">
                    <select name="tool-used" id="tool-used">
                      <option value="available" ${result.isTaken? "selected": ""} >Свободен</option>
                      <option value="taken" ${result.isTaken? "": "selected"}>В работе</option>
                    </select>
                    <img class="fav-image" src="pics/heart-red.png">
                    <img class="fav-image" src="pics/gear.png">
                  </div>
                </div>
                <div class="id-container">
                  <span>${result.code}</span><img src="pics/circle.png"></img ><span>${result.serial_number}</span>
                </div>
              </div>
        `)
    })
    .catch((err) => {
        console.log(err)
        console.log("An error occured while fetching.")
    })
};

const getLi = (usages) => {
  usages_new = ''
  usages.split('\r\n').map(usage => {
      usages_new += `<li><span class="usage-type">${usage.split(':')[0]}</span><span class="usage-property">: ${usage.split(':')[1]}<span></li>`
  })
  return usages_new
}

const getUsage = async (id) => {
  fetch(`https://biotech-task.herokuapp.com/usage/get/${id}`,
        {
            method: "GET",
        }
    ).then(response => response.json())
    .then(data => {
        // console.log(data)
        data.results.map(result => {
          $('.usage-panel').append(`
            <div class="usage-item">
              <div class="date">
                <span>${result.start_date}</span>
              </div>
              <div class="type">
                <span class="work-in-process">В работе</span>
                <br>
                <span>${result.type}</span>
              </div>
              <div class="usage">
                <ul>
                  ${getLi(result.usage)}
                </ul>
              </div>
              <div class="result">
                <span>${result.result}</span>
                <img src="pics/mark.png" />
              </div>
              <div class="username">
                <span>${result.username}</span>
              </div>
            </div>
          `)
        })
    })
    .catch((err) => {
        console.log(err)
        console.log("An error occured while fetching.")
    })
};

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
id = urlParams.get('id')

getTool(id)
getUsage(id)

const date_shortcuts = [1, 7, 14, 30, 90, 180]

const paintGreen = (id) => {
  $('.dates-shortcuts span').removeClass("light-green");
  $('.dates-shortcuts span').eq(id).addClass("light-green");
  date_end = new Date()
  date_start = new Date(new Date().getTime() - (date_shortcuts[id]*24*60*60*1000));
  filter(date_start, date_end)
}

var date_start = new Date('0001-01-01T12:00')
var date_end = new Date('9999-01-01T12:00')

const filter = (date_start, date_end) => {
    $('.usage-item').map(i => {
      console.log(date_start, date_end)
      let current_date = new Date($('.usage-item .date span').eq(i).text())

      if ((date_start <= current_date) && (date_end >= current_date)) {
        $('.usage-item').eq(i).css('display', 'flex')
      } else {
        $('.usage-item').eq(i).css('display', 'none')
      }
    })
}


$( "#date-1" ).change('input', function() {
  date_start  = new Date($(this).val())
  $('.dates-shortcuts span').removeClass("light-green");
  filter(date_start, date_end)
});

$( "#date-2" ).change('input', function() {
  date_end  = new Date($(this).val())
  $('.dates-shortcuts span').removeClass("light-green");
  filter(date_start, date_end)
});
