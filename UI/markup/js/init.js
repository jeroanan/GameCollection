// Copyright (c) 2015 David Wilson
// Icarus is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// Icarus is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

requirejs.config({
	 urlArgs: "bust=20150706233115",
	 baseUrl: '/static/js',
	 paths: {
		  jquery: ['https://code.jquery.com/jquery-2.1.4.min', 'jquery-2.1.4.min'],
		  jqueryui: 'jquery-ui.min',
		  jquerycookie: 'jquery.cookie-1.4.1.min',
		  'bootstrap.min': 'bootstrap.min'
	 }
});

require(['jquery'], function () {
	 require(['jqueryui', 'jquerycookie', 'bootstrap.min'], function () {
		  require(['script.min']);
	 });
});
