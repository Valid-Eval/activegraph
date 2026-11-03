Rails.application.routes.draw do
  resources :stages, only: [:show]
end
