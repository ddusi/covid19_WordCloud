function infoData() {
  let contents = [];

  function saveContentData(list) {
    const children = [...list].map(({ children }) => children);
    contents = children.map(([summary, content]) => ({
      summary: summary.textContent,
      content: content.textContent,
    }));
  }
  function getContents() {
    return contents;
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
  function setMaxPageNumber(contentsPerPage = 10) {
    maxPageNumber = Math.ceil(contents.length / contentsPerPage);
  }
  function getMaxPageNumber() {
    return maxPageNumber;
  }
  function getCurrentPage() {
    return pageNumber;
  }

  return {
    saveContentData,
    getContents,
    previousPage,
    nextPage,
    setPage,
    setMaxPageNumber,
    getMaxPageNumber,
    getCurrentPage,
  };
};

function infoView() {
  function displayContents(list, currentPage, contentsPerPage = 10) {
    if (list.length === 0) {
      console.error('The content list is empty!');
      return;
    }

    const contents = list[0].parentNode.children;
    const START_INDEX = (currentPage - 1) * contentsPerPage;
    const END_INDEX = currentPage * contentsPerPage;

    for (let i = 0, len = contents.length; i < len; i++) {
      let content = contents[i];

      if (i < START_INDEX || i >= END_INDEX) {
        content.classList.add('hidden');
      } else {
        content.classList.remove('hidden');
      }
    }
  }

  const PAGE_BUTTON_CONTAINER_CLASSNAME = 'info-contents__page-buttons--container';
  const PAGE_BUTTON_CLASSNAME = 'page-buttons__button';
  function displayPageButtons(maxPageNumber, currentPage, parentElm) {
    if (maxPageNumber <= 1) {
      console.log('Page buttons are not created as contents fit in a single page.');
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

    parentElm.prepend(container);
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
    displayContents,
    displayPageButtons,
    emphasizeCurrentPage,
    PAGE_BUTTON_CLASSNAME,
    PAGE_BUTTON_CONTAINER_CLASSNAME,
  };
}

function infoController() {
  const CONTENTS = document.querySelectorAll('.content--container');
  const CONTENT_SECTION = document.querySelector('.info__contents');
  const CONTENTS_PER_PAGE = 6;

  const INFO_DATA = infoData();
  function handleData() {
    INFO_DATA.saveContentData(CONTENTS);
    INFO_DATA.setMaxPageNumber(CONTENTS_PER_PAGE);
  }

  const INFO_VIEW = infoView();
  function firstRender() {
    INFO_VIEW.displayContents(CONTENTS, INFO_DATA.getCurrentPage(), CONTENTS_PER_PAGE);
    INFO_VIEW.displayPageButtons(INFO_DATA.getMaxPageNumber(), INFO_DATA.getCurrentPage(), CONTENT_SECTION);
    INFO_VIEW.emphasizeCurrentPage(INFO_DATA.getCurrentPage());
  }
  function updateRender() {
    INFO_VIEW.displayContents(CONTENTS, INFO_DATA.getCurrentPage(), CONTENTS_PER_PAGE);
    INFO_VIEW.emphasizeCurrentPage(INFO_DATA.getCurrentPage());
  }

  function activateButtons() {
    const BUTTON_CONTAINER = document.querySelector(`.${INFO_VIEW.PAGE_BUTTON_CONTAINER_CLASSNAME}`);
    BUTTON_CONTAINER.addEventListener('click', ({ target }) => {
      if (target.className !== INFO_VIEW.PAGE_BUTTON_CLASSNAME) return;

      const SELECTED_PAGE = parseInt(target.textContent);
      INFO_DATA.setPage(SELECTED_PAGE);
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
  const CONTROLLER = infoController();
  CONTROLLER.handleData();
  CONTROLLER.firstRender();
  CONTROLLER.activateButtons();
}

document.addEventListener('DOMContentLoaded', init);