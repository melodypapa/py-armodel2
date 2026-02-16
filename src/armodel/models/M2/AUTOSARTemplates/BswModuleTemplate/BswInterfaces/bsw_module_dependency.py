"""BswModuleDependency AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
    BswModuleDescription,
)


class BswModuleDependency(Identifiable):
    """AUTOSAR BswModuleDependency."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("target_module_id", None, True, False, None),  # targetModuleId
        ("target_module", None, False, False, BswModuleDescription),  # targetModule
    ]

    def __init__(self) -> None:
        """Initialize BswModuleDependency."""
        super().__init__()
        self.target_module_id: Optional[PositiveInteger] = None
        self.target_module: Optional[BswModuleDescription] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModuleDependency to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleDependency":
        """Create BswModuleDependency from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModuleDependency instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModuleDependency since parent returns ARObject
        return cast("BswModuleDependency", obj)


class BswModuleDependencyBuilder:
    """Builder for BswModuleDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleDependency = BswModuleDependency()

    def build(self) -> BswModuleDependency:
        """Build and return BswModuleDependency object.

        Returns:
            BswModuleDependency instance
        """
        # TODO: Add validation
        return self._obj
