"""RptExecutableEntityProperties AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class RptExecutableEntityProperties(ARObject):
    """AUTOSAR RptExecutableEntityProperties."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_rpt_event_id", None, True, False, None),  # maxRptEventId
        ("min_rpt_event_id", None, True, False, None),  # minRptEventId
        ("rpt_execution_control", None, False, False, RptExecutionControlEnum),  # rptExecutionControl
        ("rpt_service_point_enum", None, False, False, RptServicePointEnum),  # rptServicePointEnum
    ]

    def __init__(self) -> None:
        """Initialize RptExecutableEntityProperties."""
        super().__init__()
        self.max_rpt_event_id: Optional[PositiveInteger] = None
        self.min_rpt_event_id: Optional[PositiveInteger] = None
        self.rpt_execution_control: Optional[RptExecutionControlEnum] = None
        self.rpt_service_point_enum: Optional[RptServicePointEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RptExecutableEntityProperties to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptExecutableEntityProperties":
        """Create RptExecutableEntityProperties from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RptExecutableEntityProperties instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RptExecutableEntityProperties since parent returns ARObject
        return cast("RptExecutableEntityProperties", obj)


class RptExecutableEntityPropertiesBuilder:
    """Builder for RptExecutableEntityProperties."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptExecutableEntityProperties = RptExecutableEntityProperties()

    def build(self) -> RptExecutableEntityProperties:
        """Build and return RptExecutableEntityProperties object.

        Returns:
            RptExecutableEntityProperties instance
        """
        # TODO: Add validation
        return self._obj
