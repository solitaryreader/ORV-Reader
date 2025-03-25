let ChapterList = [];
function addAllChapters() {
    fetch('../../meta/orv_titles.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            ChapterList.push(...data);
            ChapterList = ChapterList.slice().sort((a, b) => b.index - a.index)
            console.log("Chapters loaded:", ChapterList);
            displayChapters();
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

function displayChapters() {
    let chapterSearch = document.getElementById("chapter-result");
    chapterSearch.innerHTML = "";
    let chSearchresult = [];

    ChapterList.forEach(chapter => {
        chSearchresult.push(`<div class="chapter_item"><a href="./read/${chapter.index+1}"><p>${chapter.title}</p></a></div>`);
    });

    chapterSearch.innerHTML = chSearchresult.join("");
}

function filter() {
    ChapterList = ChapterList.slice().reverse();
    document.getElementById("search").value = ""
    console.log(document.getElementById("filter").style.transform)
    const FilterSVG = document.getElementById("filter");
    if (FilterSVG.style.transform === "rotateX(180deg)") {
        FilterSVG.style.transform = "rotateX(0deg)"
    } else {
        FilterSVG.style.transform = "rotateX(180deg)"
    }
    displayChapters()

}


function findChapter(value) {
    let chapterSearch = document.getElementById("chapter-result");
    chapterSearch.innerHTML = "";
    let chSearchresult = [];

    for (let i = 0; i < ChapterList.length; i++) {

        let title = String(ChapterList[i].title).toLowerCase();
        let chSearchindex = title.indexOf(value.toLowerCase());
        let index = ChapterList[i].index;
        if (chSearchindex !== -1) {
            chSearchresult.push(`<div class="chapter_item"><a href="./read/${index+1}"><p>${title}</p></a></div>`);
        }
    }
    chapterSearch.innerHTML = chSearchresult.join("");

    if (chSearchresult.length === 0) {
        chapterSearch.innerHTML = `<div class="chapter_item"><p>Chapter not found</p></div>`;
    }
}

document.addEventListener('DOMContentLoaded', function () {
    addAllChapters();
});