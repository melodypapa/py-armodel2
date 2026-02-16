"""TDEventOccurrenceExpression AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TDEventOccurrenceExpression(ARObject):
    """AUTOSAR TDEventOccurrenceExpression."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("arguments", None, False, True, AutosarOperationArgumentInstance),  # arguments
        ("formula", None, False, False, any (TDEventOccurrence)),  # formula
        ("modes", None, False, True, TimingModeInstance),  # modes
        ("variables", None, False, True, any (AutosarVariable)),  # variables
    ]

    def __init__(self) -> None:
        """Initialize TDEventOccurrenceExpression."""
        super().__init__()
        self.arguments: list[AutosarOperationArgumentInstance] = []
        self.formula: Optional[Any] = None
        self.modes: list[TimingModeInstance] = []
        self.variables: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventOccurrenceExpression to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventOccurrenceExpression":
        """Create TDEventOccurrenceExpression from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventOccurrenceExpression instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventOccurrenceExpression since parent returns ARObject
        return cast("TDEventOccurrenceExpression", obj)


class TDEventOccurrenceExpressionBuilder:
    """Builder for TDEventOccurrenceExpression."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventOccurrenceExpression = TDEventOccurrenceExpression()

    def build(self) -> TDEventOccurrenceExpression:
        """Build and return TDEventOccurrenceExpression object.

        Returns:
            TDEventOccurrenceExpression instance
        """
        # TODO: Add validation
        return self._obj
