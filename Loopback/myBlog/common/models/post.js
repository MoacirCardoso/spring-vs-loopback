'use strict';

module.exports = Post => {
  Post.observe('before save', (ctx, next) => {
    if (ctx.instance) {
      ctx.instance.createdAt = new Date();
    } else {
      ctx.data.createdAt = new Date();
    }
    next();
  });

  Post.observe('before update', (ctx, next) => {
    if (ctx.instance) {
      ctx.instance.updateAt = new Date();
    } else {
      ctx.data.updateAt = new Date();
    }
    next();
  });
};
