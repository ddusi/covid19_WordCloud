
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
  function setPage(number) {
    pageNumber = number;
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
    setPage,
    setMaxPageNumber,
    getMaxPageNumber,
    getCurrentPage,
  };
};

function newsView() {
  function displayArticles(list, currentPage, articlesPerPage = 10) {
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

  const PAGE_BUTTON_CONTAINER_CLASSNAME = 'article-list__page-buttons--container';
  const PAGE_BUTTON_CLASSNAME = 'page-buttons__button';
  function displayPageButtons(maxPageNumber, currentPage, parentElm) {
    if (maxPageNumber <= 1) {
      console.log('Page buttons are not created as articles fit in a single page.');
      return;
    }

    let container = document.createElement('div');
    container.className = PAGE_BUTTON_CONTAINER_CLASSNAME;

    for (let i = 1; i <= maxPageNumber; i++) {
      let pageButton = document.createElement('span');
      pageButton.textContent = i;
      pageButton.className = PAGE_BUTTON_CLASSNAME;
      container.appendChild(pageButton);
    }

    parentElm.appendChild(container);
  }

  function emphasizeCurrentPage(currentPage) {
    const buttons = document.querySelectorAll(`.${PAGE_BUTTON_CLASSNAME}`);

    for (let i = 0, len = buttons.length; i < len; i++) {
      if (i === currentPage - 1) {
        buttons[i].classList.add('active');
      } else {
        buttons[i].classList.remove('active');
      }
    }
  }

  return {
    displayArticles,
    displayPageButtons,
    emphasizeCurrentPage,
    PAGE_BUTTON_CLASSNAME,
    PAGE_BUTTON_CONTAINER_CLASSNAME,
  };
}

function newsController() {
  const ARTICLES = document.querySelectorAll('.article-table__article');
  const ARTICLE_SECTION = document.querySelector('.news__article-list--container');
  const ARTICLES_PER_PAGE = 10;

  const NEWS_DATA = newsData();
  function handleData() {
    NEWS_DATA.saveArticleData(ARTICLES);
    NEWS_DATA.setMaxPageNumber(ARTICLES_PER_PAGE);
  }

  const NEWS_VIEW = newsView();
  function firstRender() {
    NEWS_VIEW.displayArticles(ARTICLES, NEWS_DATA.getCurrentPage(), ARTICLES_PER_PAGE);
    NEWS_VIEW.displayPageButtons(NEWS_DATA.getMaxPageNumber(), NEWS_DATA.getCurrentPage(), ARTICLE_SECTION);
    NEWS_VIEW.emphasizeCurrentPage(NEWS_DATA.getCurrentPage());
  }
  function updateRender() {
    NEWS_VIEW.displayArticles(ARTICLES, NEWS_DATA.getCurrentPage(), ARTICLES_PER_PAGE);
    NEWS_VIEW.emphasizeCurrentPage(NEWS_DATA.getCurrentPage());
  }

  function activateButtons() {
    const BUTTON_CONTAINER = document.querySelector(`.${NEWS_VIEW.PAGE_BUTTON_CONTAINER_CLASSNAME}`);
    BUTTON_CONTAINER.addEventListener('click', ({ target }) => {
      if (target.className !== NEWS_VIEW.PAGE_BUTTON_CLASSNAME) return;

      const SELECTED_PAGE = parseInt(target.textContent);
      NEWS_DATA.setPage(SELECTED_PAGE);
      updateRender();
    })
  }

  return {
    handleData,
    firstRender,
    updateRender,
    activateButtons,
  };
}

function init() {
  const CONTROLLER = newsController();
  CONTROLLER.handleData();
  CONTROLLER.firstRender();
  CONTROLLER.activateButtons();
}

document.addEventListener('DOMContentLoaded', init);