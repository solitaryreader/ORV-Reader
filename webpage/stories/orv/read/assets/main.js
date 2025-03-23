const ChapterList = [];
let chFetchStatus = false;


function addAllChapters() {

  if (!chFetchStatus) {
    fetch('../../../meta/titles.json')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        ChapterList.push(...data);
        console.log("Chapters loaded:", ChapterList);
        chFetchStatus = true;

      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
      })
      .then(() => {
        let chapterSearch = document.getElementById("chapter-search-reasult");
        let chapterTitle = document.getElementsByClassName("orv_title")[0].textContent.trim();
        let chapterID = "";
        let chSearchresult = [];

        ChapterList.forEach(chapter => {
          if (chapterTitle === chapter.title) {
            chapterID = "current-chapter";
            chapter.index = "";
          }
          chSearchresult.push(`<div class="chapter_item" id="${chapterID}"><p><a href="#${chapter.index}">${chapter.title}</a></p></div>`);
          chapterID = "";
        });

        chapterSearch.innerHTML = chSearchresult.join("");
        document.getElementById("current-chapter").scrollIntoView({ behavior: "smooth", block: "center" });
      });
  }
}

function openChapters() {
  addAllChapters()
  document.getElementById('chapters').style.display = 'block'
}



function findChapter() {
  let chapter = document.getElementById("find-chapter").value.trim();
  let chapterSearch = document.getElementById("chapter-search-reasult")
  chapterSearch.innerHTML = ""
  let chSearchresult = []

  for (let i = 0; i < ChapterList.length; i++) {
    let title = String(ChapterList[i].title).toLowerCase();
    let chSearchindex = title.indexOf(chapter.toLowerCase());
    let index = ChapterList[i].index;
    if (chSearchindex !== -1) {
      chSearchresult.push(`<div class="chapter_item"><p><a href="#${index}">${title}</a></p></div>`);
    }

  }
  chapterSearch.innerHTML = chSearchresult.join("");

  if (chSearchresult.length === 0) {
    chapterSearch.innerHTML = `<div class="chapter_item"><p>Chapter not found</p></div>`;
  }
}


// function handleClick(event) {
//   console.log("Element clicked:", event.target);
// }

// document.getElementById("yourElementId").addEventListener("click", handleClick);