"""ObdMonitorServiceNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)


class ObdMonitorServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdMonitorServiceNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("application_data", None, False, False, ApplicationDataType),  # applicationData
        ("event_needs", None, False, False, DiagnosticEventNeeds),  # eventNeeds
        ("unit_and_scaling_id", None, True, False, None),  # unitAndScalingId
        ("update_kind", None, False, False, DiagnosticMonitorUpdateKindEnum),  # updateKind
    ]

    def __init__(self) -> None:
        """Initialize ObdMonitorServiceNeeds."""
        super().__init__()
        self.application_data: Optional[ApplicationDataType] = None
        self.event_needs: Optional[DiagnosticEventNeeds] = None
        self.unit_and_scaling_id: Optional[PositiveInteger] = None
        self.update_kind: Optional[DiagnosticMonitorUpdateKindEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ObdMonitorServiceNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdMonitorServiceNeeds":
        """Create ObdMonitorServiceNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ObdMonitorServiceNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ObdMonitorServiceNeeds since parent returns ARObject
        return cast("ObdMonitorServiceNeeds", obj)


class ObdMonitorServiceNeedsBuilder:
    """Builder for ObdMonitorServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdMonitorServiceNeeds = ObdMonitorServiceNeeds()

    def build(self) -> ObdMonitorServiceNeeds:
        """Build and return ObdMonitorServiceNeeds object.

        Returns:
            ObdMonitorServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
