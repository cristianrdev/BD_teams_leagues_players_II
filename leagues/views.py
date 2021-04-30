from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
	if request.method == 'GET':
		print('------------es un GET-----------------')
		context = {
			"leagues": League.objects.all(),
			"teams": Team.objects.all(),
			"players": Player.objects.all(),
			"title_leagues": '',
			"title_teams": '',
			"title_players": '',
		}
		return render(request, "leagues/index.html", context)
	
	else:
		print('------------es un POST-----------------')




		if int(request.POST['filtro']) == 1 :
			print('es el filtro 1***********')
			context = {
			"title_leagues": 'hidden',
			"teams": Team.objects.filter(league__name = "Atlantic Soccer Conference"),
			"title_players": 'hidden',

			}

		if int(request.POST['filtro']) == 2 :
			print('es el filtro 2***********')
			context = {
				"title_leagues": 'hidden',
				"title_teams": 'hidden',
				"players": Player.objects.filter(curr_team__team_name='Penguins'),
			}
			

		if int(request.POST['filtro']) == 3 :
			print('es el filtro 3***********')
			context = {
				"title_leagues": 'hidden',
				"title_teams": 'hidden',
				"players": Player.objects.filter(curr_team__league__name='International Collegiate Baseball Conference'),
			}

		if int(request.POST['filtro']) == 4 :
			print('es el filtro 4***********')
			jugadores_de_la_liga = Player.objects.filter(curr_team__league__name='American Conference of Amateur Football')
			context = {

				"title_leagues": 'hidden',
				"title_teams": 'hidden',
				"players": jugadores_de_la_liga.filter(last_name='Lopez'),
			}

		if int(request.POST['filtro']) == 5 :
			print('es el filtro 5***********')
			context = {
				"title_leagues": 'hidden',
				"title_teams": 'hidden',
				"players": Player.objects.filter(curr_team__league__sport='Football'),
			}

		if int(request.POST['filtro']) == 6 :
			print('es el filtro 6***********')
			context = {
				"title_leagues": 'hidden',
				"teams": Team.objects.filter(curr_players__first_name='Sophia'),
				"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 7 :
			print('es el filtro 7***********')
			context = {
			"leagues": League.objects.filter(teams__curr_players__first_name='Sophia'),
			"title_teams": 'hidden',
			"title_players": 'hidden',
			
			}

		if int(request.POST['filtro']) == 8 :
			print('es el filtro 8***********')
			context = {
				"title_leagues": 'hidden',
				"title_teams": 'hidden',
				"players": Player.objects.filter(last_name='Flores').exclude(all_teams__team_name='Roughriders'),
			}

		if int(request.POST['filtro']) == 9 :
			print('es el filtro 9***********')
			context = {
			"title_leagues": 'hidden',
			"teams": Team.objects.filter(all_players__first_name='Samuel').filter(all_players__last_name='Evans'),
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 10 :
			print('es el filtro 10***********')
			context = {
				"title_leagues": 'hidden',
				"title_teams": 'hidden',
				"players": Player.objects.filter(all_teams__team_name='Tiger-Cats').filter(all_teams__location='Manitoba'),
			}

		if int(request.POST['filtro']) == 11 :
			print('es el filtro 11***********')
			context = {
				"title_leagues": 'hidden',
				"title_teams": 'hidden',
				"players": Player.objects.filter(all_teams__team_name='Vikings').exclude(curr_team__team_name='Vikings'),
			}

		if int(request.POST['filtro']) == 12 :
			print('es el filtro 12***********')
			context = {
			"title_leagues": 'hidden',
			"teams": Team.objects.filter(all_players__first_name='Jacob').filter(all_players__last_name='Gray').exclude(curr_players__first_name='Jacob').exclude(curr_players__last_name='Gray'),
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 13 :
			print('es el filtro 13***********')
			context = {
				"title_leagues": 'hidden',
				"title_teams": 'hidden',
				"players": Player.objects.filter(first_name='Joshua').filter(all_teams__league__name='Atlantic Federation of Amateur Baseball Players'),
			}

		if int(request.POST['filtro']) == 14 :
			print('es el filtro 14***********')
			context = {
			"title_leagues": 'hidden',
			"teams": Team.objects.annotate(contador = Count('all_players')).filter(contador__gt=11),
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 15 :
			print('es el filtro 15***********')
			# jugadores_cooper = Player.objects.
			context = {
			"title_leagues": 'hidden',
			"title_teams": 'hidden',
			"players":  Player.objects.annotate(contador = Count('all_teams')).order_by('-contador'),

			}



		return render(request, "leagues/index.html", context)


def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")