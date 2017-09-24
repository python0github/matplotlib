# -*- coding: utf-8 -*-
import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories'
url += '?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', str(r.status_code))
response_dict = r.json()
print('Total repositories: ', str(response_dict['total_count']))

# 研究有关仓库的信息
repo_dicts = response_dict['items']
names, plot_dicts = [], []  # 创建空列表
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
            'value': repo_dict['stargazers_count'],
            'xlink': repo_dict['html_url'],
            'label': str(repo_dict['description']),
            }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_lablel = 15
my_config.show_y_guides = False
my_config.width = 1000

# 创建图表
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Project on GitHub'

chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
