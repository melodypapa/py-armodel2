"""Schema comparator for comparing JSON class definitions against XSD schema."""

from typing import Dict, List, Optional

from tools.validation.models import (
    Discrepancy,
    DiscrepancySeverity,
    DiscrepancyType,
    JSONClass,
    JSONMember,
    XSDComplexType,
    XSDMember,
)


class SchemaComparator:
    """Comparator for JSON and XSD schema definitions."""

    def __init__(self, skip_classes: Optional[set[str]] = None):
        """Initialize schema comparator.

        Args:
            skip_classes: Set of class names to skip (manually maintained)
        """
        self.skip_classes = skip_classes or set()
        self.discrepancies: List[Discrepancy] = []

    def compare_all(
        self,
        json_classes: Dict[str, JSONClass],
        xsd_types: Dict[str, XSDComplexType],
    ) -> List[Discrepancy]:
        """Compare all JSON classes against XSD types.

        Args:
            json_classes: Dictionary of JSON classes
            xsd_types: Dictionary of XSD complex types

        Returns:
            List of discrepancies
        """
        self.discrepancies = []

        for class_name, json_class in json_classes.items():
            # Skip manually maintained classes
            if class_name in self.skip_classes:
                continue

            # Check if class exists in XSD
            if class_name not in xsd_types:
                self.discrepancies.append(
                    Discrepancy(
                        discrepancy_type=DiscrepancyType.MISSING_XSD_TYPE,
                        severity=DiscrepancySeverity.INFO,
                        class_name=class_name,
                        member_name=None,
                        message="Class not found in XSD schema (may be manually maintained or from different schema version)",
                    )
                )
                continue

            xsd_type = xsd_types[class_name]
            self._compare_class(json_class, xsd_type)

        return self.discrepancies

    def _compare_class(self, json_class: JSONClass, xsd_type: XSDComplexType) -> None:
        """Compare a single JSON class against XSD type.

        Args:
            json_class: JSON class definition
            xsd_type: XSD complex type definition
        """
        # Compare members
        json_members = json_class.attributes
        xsd_members = xsd_type.members

        # Check for missing members (in XSD but not in JSON)
        for member_name, xsd_member in xsd_members.items():
            if member_name not in json_members:
                severity = DiscrepancySeverity.ERROR if xsd_member.multiplicity == "1" else DiscrepancySeverity.WARNING
                self.discrepancies.append(
                    Discrepancy(
                        discrepancy_type=DiscrepancyType.MISSING_MEMBER,
                        severity=severity,
                        class_name=json_class.name,
                        member_name=member_name,
                        message="Member exists in XSD but not in JSON",
                        details={
                            "xsd_member_name": member_name,
                            "xsd_type": self._normalize_type(xsd_member.type_name),
                            "xsd_multiplicity": xsd_member.multiplicity,
                            "xsd_reference_kind": xsd_member.reference_kind or "none",
                        },
                    )
                )

        # Check for extra members (in JSON but not in XSD)
        for member_name, json_member in json_members.items():
            if member_name not in xsd_members:
                severity = DiscrepancySeverity.ERROR if json_member.multiplicity == "1" else DiscrepancySeverity.INFO
                self.discrepancies.append(
                    Discrepancy(
                        discrepancy_type=DiscrepancyType.EXTRA_MEMBER,
                        severity=severity,
                        class_name=json_class.name,
                        member_name=member_name,
                        message="Member exists in JSON but not in XSD",
                        details={
                            "json_type": json_member.type,
                            "json_multiplicity": json_member.multiplicity,
                            "json_kind": json_member.kind,
                        },
                    )
                )
                continue

            # Compare member details (type, multiplicity, reference kind)
            xsd_member = xsd_members[member_name]
            self._compare_member(json_class.name, member_name, json_member, xsd_member)

    def _compare_member(
        self,
        class_name: str,
        member_name: str,
        json_member: JSONMember,
        xsd_member: XSDMember,
    ) -> None:
        """Compare a single member definition.

        Args:
            class_name: Class name
            member_name: Member name
            json_member: JSON member definition
            xsd_member: XSD member definition
        """
        # Normalize types for comparison
        json_type = self._normalize_type(json_member.type)
        xsd_type = self._normalize_type(xsd_member.type_name)

        # Compare types
        if json_type != xsd_type:
            self.discrepancies.append(
                Discrepancy(
                    discrepancy_type=DiscrepancyType.TYPE_MISMATCH,
                    severity=DiscrepancySeverity.WARNING,
                    class_name=class_name,
                    member_name=member_name,
                    message="Type differs between JSON and XSD",
                    details={
                        "json_type": json_type,
                        "json_multiplicity": json_member.multiplicity,
                        "xsd_member_name": member_name,
                        "xsd_type": xsd_type,
                        "xsd_multiplicity": xsd_member.multiplicity,
                    },
                )
            )

        # Compare multiplicity
        if json_member.multiplicity != xsd_member.multiplicity:
            severity = DiscrepancySeverity.ERROR if json_member.multiplicity == "1" or xsd_member.multiplicity == "1" else DiscrepancySeverity.WARNING
            self.discrepancies.append(
                Discrepancy(
                    discrepancy_type=DiscrepancyType.MULTIPLICITY_MISMATCH,
                    severity=severity,
                    class_name=class_name,
                    member_name=member_name,
                    message="Cardinality differs between JSON and XSD",
                    details={
                        "json_type": json_type,
                        "json_multiplicity": json_member.multiplicity,
                        "xsd_member_name": member_name,
                        "xsd_type": xsd_type,
                        "xsd_multiplicity": xsd_member.multiplicity,
                    },
                )
            )

        # Compare reference kind
        json_is_ref = json_member.is_ref
        xsd_is_ref = xsd_member.is_reference

        if json_is_ref != xsd_is_ref:
            self.discrepancies.append(
                Discrepancy(
                    discrepancy_type=DiscrepancyType.REF_KIND_MISMATCH,
                    severity=DiscrepancySeverity.WARNING,
                    class_name=class_name,
                    member_name=member_name,
                    message="Reference kind differs between JSON and XSD",
                    details={
                        "json_type": json_type,
                        "json_multiplicity": json_member.multiplicity,
                        "json_kind": json_member.kind,
                        "xsd_member_name": member_name,
                        "xsd_type": xsd_type,
                        "xsd_multiplicity": xsd_member.multiplicity,
                        "xsd_reference_kind": xsd_member.reference_kind or "none",
                    },
                )
            )

    def _normalize_type(self, type_name: str) -> str:
        """Normalize type name for comparison.

        Removes prefixes and suffixes that are not part of the core type.

        Args:
            type_name: Raw type name

        Returns:
            Normalized type name
        """
        if not type_name:
            return ""

        # Remove AR: prefix
        if type_name.startswith("AR:"):
            type_name = type_name[3:]

        # Remove --SUBTYPES-ENUM suffix
        if type_name.endswith("--SUBTYPES-ENUM"):
            type_name = type_name[:-15]

        # Remove --SIMPLE suffix
        if type_name.endswith("--SIMPLE"):
            type_name = type_name[:-8]

        # Remove -ENUM suffix
        if type_name.endswith("-ENUM"):
            type_name = type_name[:-5]

        return type_name

    def get_summary(self) -> Dict[str, int]:
        """Get summary of discrepancies.

        Returns:
            Dictionary with counts by severity
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