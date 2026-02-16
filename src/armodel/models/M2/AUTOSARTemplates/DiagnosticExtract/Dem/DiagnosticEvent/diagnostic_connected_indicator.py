"""DiagnosticConnectedIndicator AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator.diagnostic_indicator import (
    DiagnosticIndicator,
)


class DiagnosticConnectedIndicator(Identifiable):
    """AUTOSAR DiagnosticConnectedIndicator."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("behavior_indicator_behavior_enum", None, False, False, any (DiagnosticConnected)),  # behaviorIndicatorBehaviorEnum
        ("healing_cycle", None, True, False, None),  # healingCycle
        ("indicator", None, False, False, DiagnosticIndicator),  # indicator
        ("indicator_failure", None, True, False, None),  # indicatorFailure
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticConnectedIndicator."""
        super().__init__()
        self.behavior_indicator_behavior_enum: Optional[Any] = None
        self.healing_cycle: Optional[PositiveInteger] = None
        self.indicator: Optional[DiagnosticIndicator] = None
        self.indicator_failure: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticConnectedIndicator to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticConnectedIndicator":
        """Create DiagnosticConnectedIndicator from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticConnectedIndicator instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticConnectedIndicator since parent returns ARObject
        return cast("DiagnosticConnectedIndicator", obj)


class DiagnosticConnectedIndicatorBuilder:
    """Builder for DiagnosticConnectedIndicator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticConnectedIndicator = DiagnosticConnectedIndicator()

    def build(self) -> DiagnosticConnectedIndicator:
        """Build and return DiagnosticConnectedIndicator object.

        Returns:
            DiagnosticConnectedIndicator instance
        """
        # TODO: Add validation
        return self._obj
