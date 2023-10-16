// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'PyTerrier',
  tagline: 'Build and run experiments using flexible retrieval pipelines',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://your-docusaurus-test-site.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        // blog: false,
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        style: "primary",
        title: 'PyTerrier',
        logo: {
          alt: 'PyTerrier Logo',
          src: 'img/white_logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Docs',
          },
          {to: '/blog', label: 'Blog', position: 'left'},
          {to: '/testPage', label: 'Test Page', position: 'left'},
          {
            href: 'https://github.com/terrier-org/pyterrier',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Introduction',
                to: '/docs/intro',
              },
              {
                label: 'Beginners start here!',
                to: '/docs/intro',
              },
              {
                label: 'Getting Started',
                to: '/docs/intro',
              },
              {
                label: 'Explanation & illustration',
                to: '/docs/intro',
              },
              {
                label: 'Other Modules',
                to: '/docs/intro',
              },
              {
                label: 'Other PyTerrier Plugin',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'Core Maintainers',
            items: [
              {
                label: 'Craig Macdonald - University of Glasgow',
                href: 'https://www.dcs.gla.ac.uk/~craigm/',
              },
              {
                label: 'Nicola Tonellotto - University of Pisa',
                href: 'https://tonellotto.github.io/',
              },
              {
                label: 'Sean MacAvaney - University of Glasgow',
                href: 'https://macavaney.us/',
              },
              {
                label: 'Iadh Ounis - University of Glasgow',
                href: 'https://www.dcs.gla.ac.uk/~ounis/',
              },
            ],
          },
          // {
          //   title: 'Thanks to Contributors!',
          //   items: [
          //     {
          //       label: 'Craig Macdonald - University of Glasgow',
          //       href: 'https://www.dcs.gla.ac.uk/~craigm/',
          //     },
          //     {
          //       label: 'Nicola Tonellotto - University of Pisa',
          //       href: 'https://tonellotto.github.io/',
          //     },
          //   ],
          // },
          {
            title: 'More',
            items: [
              {
                label: 'Blog',
                to: '/blog',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/terrier-org/pyterrier',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
