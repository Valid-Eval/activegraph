class StagesController < ApplicationController
  before_action :load_stage

  def show
    render json: @stage.summary
  end

  private

  def load_stage
    @stage = Stage.find(params[:id])
  end
end
