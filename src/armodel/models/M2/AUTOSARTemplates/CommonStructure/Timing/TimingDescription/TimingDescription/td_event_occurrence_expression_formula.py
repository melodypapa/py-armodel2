"""TDEventOccurrenceExpressionFormula AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TDEventOccurrenceExpressionFormula(ARObject):
    """AUTOSAR TDEventOccurrenceExpressionFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("argument", None, False, False, AutosarOperationArgumentInstance),  # argument
        ("event", None, False, False, TimingDescriptionEvent),  # event
        ("mode", None, False, False, TimingModeInstance),  # mode
        ("variable", None, False, False, any (AutosarVariable)),  # variable
    ]

    def __init__(self) -> None:
        """Initialize TDEventOccurrenceExpressionFormula."""
        super().__init__()
        self.argument: Optional[AutosarOperationArgumentInstance] = None
        self.event: Optional[TimingDescriptionEvent] = None
        self.mode: Optional[TimingModeInstance] = None
        self.variable: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventOccurrenceExpressionFormula to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventOccurrenceExpressionFormula":
        """Create TDEventOccurrenceExpressionFormula from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventOccurrenceExpressionFormula instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventOccurrenceExpressionFormula since parent returns ARObject
        return cast("TDEventOccurrenceExpressionFormula", obj)


class TDEventOccurrenceExpressionFormulaBuilder:
    """Builder for TDEventOccurrenceExpressionFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventOccurrenceExpressionFormula = TDEventOccurrenceExpressionFormula()

    def build(self) -> TDEventOccurrenceExpressionFormula:
        """Build and return TDEventOccurrenceExpressionFormula object.

        Returns:
            TDEventOccurrenceExpressionFormula instance
        """
        # TODO: Add validation
        return self._obj
