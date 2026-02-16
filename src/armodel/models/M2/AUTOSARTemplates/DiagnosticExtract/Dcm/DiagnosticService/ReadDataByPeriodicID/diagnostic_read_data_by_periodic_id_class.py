"""DiagnosticReadDataByPeriodicIDClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDataByPeriodicID.diagnostic_periodic_rate import (
    DiagnosticPeriodicRate,
)


class DiagnosticReadDataByPeriodicIDClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadDataByPeriodicIDClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_periodic_did", None, True, False, None),  # maxPeriodicDid
        ("periodic_rates", None, False, True, DiagnosticPeriodicRate),  # periodicRates
        ("scheduler_max", None, True, False, None),  # schedulerMax
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByPeriodicIDClass."""
        super().__init__()
        self.max_periodic_did: Optional[PositiveInteger] = None
        self.periodic_rates: list[DiagnosticPeriodicRate] = []
        self.scheduler_max: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticReadDataByPeriodicIDClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByPeriodicIDClass":
        """Create DiagnosticReadDataByPeriodicIDClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticReadDataByPeriodicIDClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticReadDataByPeriodicIDClass since parent returns ARObject
        return cast("DiagnosticReadDataByPeriodicIDClass", obj)


class DiagnosticReadDataByPeriodicIDClassBuilder:
    """Builder for DiagnosticReadDataByPeriodicIDClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByPeriodicIDClass = DiagnosticReadDataByPeriodicIDClass()

    def build(self) -> DiagnosticReadDataByPeriodicIDClass:
        """Build and return DiagnosticReadDataByPeriodicIDClass object.

        Returns:
            DiagnosticReadDataByPeriodicIDClass instance
        """
        # TODO: Add validation
        return self._obj
