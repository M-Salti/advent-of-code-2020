// #define _GLIBCXX_DEBUG
#include <bits/stdc++.h>

using namespace std;

const int inf = 1234567890;
const int dr[] = {1, 1, 1, -1, -1, -1, 0, 0};
const int dc[] = {0, 1, -1, 0, 1, -1, 1, -1};

int nrows, ncols;

auto in_grid = [](int i, int j) { return i >= 0 && j >= 0 && i < nrows && j < ncols; };

vector<string> apply_step(const vector<string>& grid, int rules_type) {
  int num_steps = -1;
  int occ_thresh = -1;

  if (rules_type == 1) {
    num_steps = 1;
    occ_thresh = 4;
  } else {
    num_steps = inf;
    occ_thresh = 5;
  }

  auto new_grid = grid;

  for (int i = 0; i < nrows; ++i) {
    for (int j = 0; j < ncols; ++j) {
      const char cur = grid[i][j];
      if (cur == '.') continue;
      int filled = 0;
      for (int d = 0; d < 8; ++d) {
        int ii = i, jj = j;
        for (int s = 0; s < num_steps; ++s) {
          ii += dr[d], jj += dc[d];
          if (!in_grid(ii, jj)) break;
          if (grid[ii][jj] != '.') {
            filled += grid[ii][jj] == '#';
            break;
          }
        }
      }
      if (cur == '#' && filled >= occ_thresh) {
        new_grid[i][j] = 'L';
      }
      else if (cur == 'L' && filled == 0) {
        new_grid[i][j] = '#';
      }
    }
  }

  return new_grid;
}

int count_filled(vector<string> grid, int rules_type) {
  nrows = grid.size();
  ncols = grid[0].size();

  while (true) {
    auto new_grid = apply_step(grid, rules_type);
    if (new_grid == grid) {
      break;
    }
    grid = new_grid;
  }

  int ans = 0;
  for (auto& i : grid) {
    for (auto& j : i) {
      ans += (j == '#');
    }
  }

  return ans;
}

vector<string> read_input(const string fn) {
  vector<string> grid;
  string temp;
  ifstream reader(fn);
  while (reader >> temp) {
    grid.emplace_back(temp);
  }
  return grid;
}

int main() {
  // test cases
  auto grid = read_input("sample");
  assert(count_filled(grid, 1) == 37);
  assert(count_filled(grid, 2) == 26);
  // 

  grid = read_input("in");
  cout << count_filled(grid, 1) << endl;
  cout << count_filled(grid, 2) << endl;

  return 0;
}
