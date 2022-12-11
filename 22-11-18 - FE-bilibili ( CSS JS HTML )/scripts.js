const ACTIVE = 'active';

const active_video = document.querySelectorAll(
  '.main-structure .content video'
);

const active_video_overlay = document.querySelector(
  '.main-structure .content .video-overlay'
);

const logo = document.querySelector('header .menu-logo');
const structure = document.querySelector('.main-structure');
const h1 = document.querySelector('.content .text-description h1');
const h2 = document.querySelector('.content .text-description h2');
const p = document.querySelector('.content .text-description p');
const menu_button = document.querySelectorAll('.aside-menu a');

active_video[0].classList.remove(ACTIVE);
active_video[0].classList.add(ACTIVE);
active_video_overlay.className = 'video-overlay video-overlay-island';

h1.innerHTML = CONTENT_INFO.island.h1;
h2.innerHTML = CONTENT_INFO.island.h2;
p.innerHTML = CONTENT_INFO.island.p;

logo.addEventListener('click', () => {
  logo.classList.toggle(ACTIVE);
  structure.classList.toggle(ACTIVE);
});

menu_button.forEach((button, index) => {
  button.addEventListener('click', () => {
    console.log(button, index);
    active_video.forEach((video) => {
      video.classList.remove(ACTIVE);
    });
    active_video[index].classList.add(ACTIVE);
    modify_content(index);
  });
});

const modify_content = (index) => {
  switch (index) {
    case 0:
      h1.innerHTML = CONTENT_INFO.island.h1;
      h2.innerHTML = CONTENT_INFO.island.h2;
      p.innerHTML = CONTENT_INFO.island.p;
      active_video_overlay.className = 'video-overlay video-overlay-island';
      break;
    case 1:
      h1.innerHTML = CONTENT_INFO.spring.h1;
      h2.innerHTML = CONTENT_INFO.spring.h2;
      p.innerHTML = CONTENT_INFO.spring.p;
      active_video_overlay.className = 'video-overlay video-overlay-spring';
      break;
    case 2:
      h1.innerHTML = CONTENT_INFO.summer.h1;
      h2.innerHTML = CONTENT_INFO.summer.h2;
      p.innerHTML = CONTENT_INFO.summer.p;
      active_video_overlay.className = 'video-overlay video-overlay-summer';
      break;
    case 3:
      h1.innerHTML = CONTENT_INFO.autumn.h1;
      h2.innerHTML = CONTENT_INFO.autumn.h2;
      p.innerHTML = CONTENT_INFO.autumn.p;
      active_video_overlay.className = 'video-overlay video-overlay-autumn';
      break;
    case 4:
      h1.innerHTML = CONTENT_INFO.winter.h1;
      h2.innerHTML = CONTENT_INFO.winter.h2;
      p.innerHTML = CONTENT_INFO.winter.p;
      active_video_overlay.className = 'video-overlay video-overlay-winter';
      break;
    default:
      break;
  }
};
