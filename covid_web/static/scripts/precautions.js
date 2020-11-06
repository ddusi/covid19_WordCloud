function clearWhiteSpace() {
  const QNA_CONTAINER = document.querySelector('.questions-list__body');

  if (QNA_CONTAINER.children.length !== 0) return;
  QNA_CONTAINER.textContent = '';
}

function init() {
  clearWhiteSpace();
}

document.addEventListener('DOMContentLoaded', init);