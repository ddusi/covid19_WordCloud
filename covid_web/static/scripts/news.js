const ARTICLES_PER_PAGE = 10;

function handlePage() {
  let pageNumber = 1;

  function nextPage() {
    pageNumber++;
    console.log(`Current page is: ${pageNumber}`);
  }

  function previousPage() {
    pageNumber--;
    console.log(`Current page is: ${pageNumber}`);
  }

  function getCurrentPage(operation) {
    const NEXT_PAGE = 'N';
    const PREVIOUS_PAGE = 'P';

    switch (operation) {
      case NEXT_PAGE:
        nextPage();
        break;
      case PREVIOUS_PAGE:
        previousPage();
        break;
    }

    return pageNumber;
  }

  return getCurrentPage;
}

function renderArticles(list, pageNumber, articlesPerPage = ARTICLES_PER_PAGE) {
  if (list.length === 0) return;

  const articles = list[0].parentNode.children;
  const START_INDEX = (pageNumber - 1) * articlesPerPage;
  const END_INDEX = pageNumber * articlesPerPage;

  for (let i = 0, len = articles.length; i < len; i++) {
    let article = articles[i];

    if (i < START_INDEX || i >= END_INDEX) {
      article.classList.add('hidden');
    } else {
      article.classList.remove('hidden');
    }
  }
}

function createPageButtons(list, articlesPerPage = ARTICLES_PER_PAGE) {
  const LIST_LENGTH = list.length;
  if (LIST_LENGTH <= articlesPerPage) return false;

  let container = document.createElement('div');
  const PAGES_COUNT = Math.ceil(LIST_LENGTH / articlesPerPage);

  for (let i = 1; i <= PAGES_COUNT; i++) {
    let pageButton = document.createElement('span');
    pageButton.textContent = i;
    container.appendChild(pageButton);
  }

  const CONTAINER_CLASSNAME = 'article-list__page-buttons--container';
  container.className = CONTAINER_CLASSNAME;

  return container;
}

function displayPageButtons(list, parent) {
  const BUTTONS = createPageButtons(list);
  if (!BUTTONS) return;

  parent.appendChild(BUTTONS);
}

function init() {
  const ARTICLES = document.querySelectorAll('.article-table__article');
  const ARTICLE_SECTION = document.querySelector('.news__article-list--container');
  displayPageButtons(ARTICLES, ARTICLE_SECTION);
}

document.addEventListener('DOMContentLoaded', init);