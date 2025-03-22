function applyShakingEffect(element) {
    const text = element.textContent;
    element.innerHTML = '';
  
    for (let i = 0; i < text.length; i++) {
      const letterSpan = document.createElement('span');
      if (text[i] === ' ') {
        letterSpan.classList.add('shaky-space');
        letterSpan.innerHTML = '&nbsp;';
      } else {
        letterSpan.classList.add('shaky-letter');
        letterSpan.textContent = text[i];
      }
      letterSpan.classList.add('js-shake', 'enabled');
      letterSpan.style.animationDelay = `${Math.random() * 0.7}s`;
      letterSpan.style.animationDuration = `${Math.random() * 0.6 + 0.6}s`;
      element.appendChild(letterSpan);
    }
  }
  
  const elements = document.querySelectorAll('.orv_shake');
  elements.forEach(applyShakingEffect);