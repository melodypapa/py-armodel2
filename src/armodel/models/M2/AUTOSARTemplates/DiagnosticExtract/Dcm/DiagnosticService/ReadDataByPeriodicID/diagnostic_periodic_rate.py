"""DiagnosticPeriodicRate AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDataByPeriodicID.diagnostic_periodic_rate import (
    DiagnosticPeriodicRate,
)


class DiagnosticPeriodicRate(ARObject):
    """AUTOSAR DiagnosticPeriodicRate."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("period", None, True, False, None),  # period
        ("periodic_rate", None, False, False, DiagnosticPeriodicRate),  # periodicRate
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticPeriodicRate."""
        super().__init__()
        self.period: Optional[TimeValue] = None
        self.periodic_rate: Optional[DiagnosticPeriodicRate] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticPeriodicRate to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticPeriodicRate":
        """Create DiagnosticPeriodicRate from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticPeriodicRate instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticPeriodicRate since parent returns ARObject
        return cast("DiagnosticPeriodicRate", obj)


class DiagnosticPeriodicRateBuilder:
    """Builder for DiagnosticPeriodicRate."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticPeriodicRate = DiagnosticPeriodicRate()

    def build(self) -> DiagnosticPeriodicRate:
        """Build and return DiagnosticPeriodicRate object.

        Returns:
            DiagnosticPeriodicRate instance
        """
        # TODO: Add validation
        return self._obj
