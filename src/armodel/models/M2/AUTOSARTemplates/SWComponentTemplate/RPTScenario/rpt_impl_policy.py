"""RptImplPolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class RptImplPolicy(ARObject):
    """AUTOSAR RptImplPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("rpt_enabler_impl", None, False, False, RptEnablerImplTypeEnum),  # rptEnablerImpl
        ("rpt_preparation_enum", None, False, False, RptPreparationEnum),  # rptPreparationEnum
    ]

    def __init__(self) -> None:
        """Initialize RptImplPolicy."""
        super().__init__()
        self.rpt_enabler_impl: Optional[RptEnablerImplTypeEnum] = None
        self.rpt_preparation_enum: Optional[RptPreparationEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RptImplPolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptImplPolicy":
        """Create RptImplPolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RptImplPolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RptImplPolicy since parent returns ARObject
        return cast("RptImplPolicy", obj)


class RptImplPolicyBuilder:
    """Builder for RptImplPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptImplPolicy = RptImplPolicy()

    def build(self) -> RptImplPolicy:
        """Build and return RptImplPolicy object.

        Returns:
            RptImplPolicy instance
        """
        # TODO: Add validation
        return self._obj
