"""Report generator for XSD validation results."""

from typing import Dict, List

from tools.validation.models import (
    Discrepancy,
    DiscrepancySeverity,
)


class DiscrepancyReporter:
    """Reporter for validation discrepancies."""

    # ANSI color codes for console output
    COLOR_ERROR = "\033[91m"  # Red
    COLOR_WARNING = "\033[93m"  # Yellow
    COLOR_INFO = "\033[94m"  # Blue
    COLOR_RESET = "\033[0m"  # Reset
    COLOR_BOLD = "\033[1m"  # Bold
    COLOR_DIM = "\033[2m"  # Dim

    def __init__(self, discrepancies: List[Discrepancy], use_colors: bool = True):
        """Initialize reporter.

        Args:
            discrepancies: List of discrepancies to report
            use_colors: Whether to use ANSI colors in console output
        """
        self.discrepancies = discrepancies
        self.use_colors = use_colors and self._supports_color()

    def _supports_color(self) -> bool:
        """Check if terminal supports ANSI colors."""
        import sys

        return sys.stdout.isatty()

    def _colorize(self, text: str, color: str) -> str:
        """Apply color to text if colors are enabled.

        Args:
            text: Text to colorize
            color: ANSI color code

        Returns:
            Colorized text
        """
        if self.use_colors:
            return f"{color}{text}{self.COLOR_RESET}"
        return text

    def print_console_report(self, min_severity: DiscrepancySeverity = DiscrepancySeverity.INFO) -> int:
        """Print validation report to console.

        Args:
            min_severity: Minimum severity level to include

        Returns:
            Exit code (0 if no errors, 1 otherwise)
        """
        summary = self._get_summary()
        total = summary["total"]

        # Print header
        print("=" * 70)
        print(self._colorize("VALIDATION REPORT", self.COLOR_BOLD))
        print("=" * 70)
        print(f"Total discrepancies: {total}")
        print()

        # Print summary by severity
        print("Summary:")
        print(f"  {self._colorize('ERRORS', self.COLOR_ERROR)}: {summary[DiscrepancySeverity.ERROR.value]}")
        print(f"  {self._colorize('WARNINGS', self.COLOR_WARNING)}: {summary[DiscrepancySeverity.WARNING.value]}")
        print(f"  {self._colorize('INFO', self.COLOR_INFO)}: {summary[DiscrepancySeverity.INFO.value]}")
        print()

        if total == 0:
            print(self._colorize("✓ No discrepancies found!", self.COLOR_BOLD))
            return 0

        # Filter by severity
        filtered = self._filter_by_severity(min_severity)

        # Group by severity
        errors = [d for d in filtered if d.severity == DiscrepancySeverity.ERROR]
        warnings = [d for d in filtered if d.severity == DiscrepancySeverity.WARNING]
        infos = [d for d in filtered if d.severity == DiscrepancySeverity.INFO]

        # Print errors
        if errors:
            print(self._colorize("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", self.COLOR_ERROR))
            print(self._colorize("ERRORS (Critical Issues)", self.COLOR_ERROR + self.COLOR_BOLD))
            print(self._colorize("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", self.COLOR_ERROR))
            for discrepancy in errors:
                self._print_discrepancy(discrepancy)
            print()

        # Print warnings
        if warnings:
            print(self._colorize("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", self.COLOR_WARNING))
            print(self._colorize("WARNINGS (Non-Critical Issues)", self.COLOR_WARNING + self.COLOR_BOLD))
            print(self._colorize("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", self.COLOR_WARNING))
            for discrepancy in warnings:
                self._print_discrepancy(discrepancy)
            print()

        # Print info
        if infos:
            print(self._colorize("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", self.COLOR_INFO))
            print(self._colorize("INFO (Additional Information)", self.COLOR_INFO + self.COLOR_BOLD))
            print(self._colorize("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", self.COLOR_INFO))
            for discrepancy in infos:
                self._print_discrepancy(discrepancy)
            print()

        # Return exit code
        return 1 if errors or warnings else 0

    def generate_markdown_report(self, output_path: str, min_severity: DiscrepancySeverity = DiscrepancySeverity.INFO) -> None:
        """Generate Markdown report.

        Args:
            output_path: Path to output Markdown file
            min_severity: Minimum severity level to include
        """
        summary = self._get_summary()
        filtered = self._filter_by_severity(min_severity)

        lines = [
            "# Validation Report",
            "",
            f"**Total discrepancies:** {summary['total']}",
            "",
            "## Summary",
            "",
            f"- **Errors:** {summary[DiscrepancySeverity.ERROR.value]}",
            f"- **Warnings:** {summary[DiscrepancySeverity.WARNING.value]}",
            f"- **Info:** {summary[DiscrepancySeverity.INFO.value]}",
            "",
        ]

        if summary['total'] == 0:
            lines.extend([
                "✅ No discrepancies found!",
                "",
            ])
        else:
            # Group discrepancies by class
            class_discrepancies: Dict[str, List[Discrepancy]] = {}

            for discrepancy in filtered:
                class_name = discrepancy.class_name
                if class_name not in class_discrepancies:
                    class_discrepancies[class_name] = []
                class_discrepancies[class_name].append(discrepancy)

            # Sort class names alphabetically
            for class_name in sorted(class_discrepancies.keys()):
                discrepancies = class_discrepancies[class_name]
                lines.extend(self._format_class_table(class_name, discrepancies))
                lines.append("")

        # Write to file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"Markdown report written to: {output_path}")

    def _print_discrepancy(self, discrepancy: Discrepancy) -> None:
        """Print a single discrepancy to console.

        Args:
            discrepancy: Discrepancy to print
        """
        severity_color = self._get_severity_color(discrepancy.severity)
        print(f"  {self._colorize(str(discrepancy), severity_color)}")
        print(f"    {self._colorize(discrepancy.message, self.COLOR_DIM)}")

        # Print details
        for key, value in discrepancy.details.items():
            print(f"      {key}: {value}")

    def _format_class_table(self, class_name: str, discrepancies: List[Discrepancy]) -> List[str]:
        """Format discrepancies for a single class as Markdown table.

        Args:
            class_name: Class name
            discrepancies: List of discrepancies for this class

        Returns:
            List of Markdown lines
        """
        lines = [
            f"## `{class_name}`",
            "",
            f"**Discrepancies:** {len(discrepancies)}",
            "",
            "| JSON Member Name | JSON Type | JSON Multiplicity | XSD Member Name | XSD Type | XSD Multiplicity | Issue |",
            "|---|---|---|---|---|---|---|",
        ]

        # Sort by JSON member name
        for discrepancy in sorted(discrepancies, key=lambda d: d.member_name or ""):
            json_member = discrepancy.member_name or "-"
            json_type = discrepancy.details.get("json_type", "-")
            json_multiplicity = discrepancy.details.get("json_multiplicity", "-")
            xsd_member = discrepancy.details.get("xsd_member_name", json_member)
            xsd_type = discrepancy.details.get("xsd_type", "-")
            xsd_multiplicity = discrepancy.details.get("xsd_multiplicity", "-")

            # Format issue
            issue_type = discrepancy.discrepancy_type.value.replace("_", " ").title()
            severity_emoji = {
                DiscrepancySeverity.ERROR: "❌",
                DiscrepancySeverity.WARNING: "⚠️",
                DiscrepancySeverity.INFO: "ℹ️",
            }.get(discrepancy.severity, "")

            issue = f"{severity_emoji} {issue_type}"

            lines.append(f"| {json_member} | {json_type} | {json_multiplicity} | {xsd_member} | {xsd_type} | {xsd_multiplicity} | {issue} |")

        lines.append("")
        return lines

    def _get_severity_color(self, severity: DiscrepancySeverity) -> str:
        """Get ANSI color for severity level.

        Args:
            severity: Severity level

        Returns:
            ANSI color code
        """
        if severity == DiscrepancySeverity.ERROR:
            return self.COLOR_ERROR
        elif severity == DiscrepancySeverity.WARNING:
            return self.COLOR_WARNING
        else:
            return self.COLOR_INFO

    def _get_summary(self) -> Dict[str, int]:
        """Get summary of discrepancies.

        Returns:
            Dictionary with counts
        """
        summary = {
            "total": len(self.discrepancies),
            DiscrepancySeverity.ERROR.value: 0,
            DiscrepancySeverity.WARNING.value: 0,
            DiscrepancySeverity.INFO.value: 0,
        }

        for discrepancy in self.discrepancies:
            summary[discrepancy.severity.value] += 1

        return summary

    def _filter_by_severity(self, min_severity: DiscrepancySeverity) -> List[Discrepancy]:
        """Filter discrepancies by minimum severity.

        Args:
            min_severity: Minimum severity level

        Returns:
            Filtered list of discrepancies
        """
        severity_order = {
            DiscrepancySeverity.ERROR: 0,
            DiscrepancySeverity.WARNING: 1,
            DiscrepancySeverity.INFO: 2,
        }

        min_level = severity_order[min_severity]

        return [
            d for d in self.discrepancies
            if severity_order[d.severity] <= min_level
        ]
