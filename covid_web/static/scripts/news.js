
function newsData() {
  let articles = [];

  function saveArticleData(list) {
    const children = [...list].map(({ children }) => children);
    articles = children.map(([headline, company, time]) => {
      const url = headline.querySelector('a').href;

      return {
        text: headline.textContent.trim(),
        href: url,
        company: company.textContent,
        time: time.textContent,
      };
    });
  }
  function getArticles() {
    return articles;
  }

  let pageNumber = 1;
  let maxPageNumber = 1;
  function nextPage() {
    if (pageNumber >= maxPageNumber) {
      console.error('This is the last page');
      return;
    }

    pageNumber++;
  }
  function previousPage() {
    if (pageNumber <= 1) {
      console.error('This is the first page');
      return;
    }

    pageNumber--;
  }
  function setMaxPageNumber(articlesPerPage = 10) {
    maxPageNumber = Math.ceil(articles.length / articlesPerPage);
  }
  function getMaxPageNumber() {
    return maxPageNumber;
  }
  function getCurrentPage() {
    return pageNumber;
  }

  return {
    saveArticleData,
    getArticles,
    previousPage,
    nextPage,
    setMaxPageNumber,
    getMaxPageNumber,
    getCurrentPage,
  };
};

function newsView() {
  function renderArticles(list, currentPage, articlesPerPage = 10) {
    if (list.length === 0) {
      console.error('The article list is empty!');
      return;
    }

    const articles = list[0].parentNode.children;
    const START_INDEX = (currentPage - 1) * articlesPerPage;
    const END_INDEX = currentPage * articlesPerPage;

    for (let i = 0, len = articles.length; i < len; i++) {
      let article = articles[i];

      if (i < START_INDEX || i >= END_INDEX) {
        article.classList.add('hidden');
      } else {
        article.classList.remove('hidden');
      }
    }
  }

  function renderPageButtons(maxPageNumber, parentElm) {
    if (maxPageNumber <= 1) {
      console.log('Page buttons are not created as articles fit in a single page.');
      return;
    }

    let container = document.createElement('div');
    const CONTAINER_CLASSNAME = 'article-list__page-buttons--container';
    container.className = CONTAINER_CLASSNAME;

    for (let i = 1; i <= maxPageNumber; i++) {
      let pageButton = document.createElement('span');
      pageButton.textContent = i;
      container.appendChild(pageButton);
    }

    parentElm.appendChild(container);
  }

  return {
    renderArticles,
    renderPageButtons,
  };
}

function init() {
  const ARTICLES = document.querySelectorAll('.article-table__article');
  const ARTICLE_SECTION = document.querySelector('.news__article-list--container');
  const ARTICLES_PER_PAGE = 10;

  const NEWS_DATA = newsData();
  NEWS_DATA.saveArticleData(ARTICLES);
  NEWS_DATA.setMaxPageNumber(ARTICLES_PER_PAGE);

  const RENDER = newsView();
  RENDER.renderArticles(ARTICLES, NEWS_DATA.getCurrentPage(), ARTICLES_PER_PAGE);
  debugger;
  RENDER.renderPageButtons(NEWS_DATA.getMaxPageNumber(), ARTICLE_SECTION);
}

document.addEventListener('DOMContentLoaded', init);