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


$(function() {
	 
	 $('#doExport').on('click', function(e) {		  
		  e.preventDefault();

		  var selections = [];

		  var checkBoxes = $(':checked').each(function() {
				selections.push($(this).val());
		  });

		  var d = { 'exportitems': selections };

		  if (selections.length>0) new Ajax().sendAjax(urls.getexportcollection, d);
	 });
});
