"""EcucModuleDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    CIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)


class EcucModuleDef(EcucDefinitionElement):
    """AUTOSAR EcucModuleDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("api_service_prefix", None, True, False, None),  # apiServicePrefix
        ("containers", None, False, True, EcucContainerDef),  # containers
        ("post_build_variant", None, True, False, None),  # postBuildVariant
        ("refined_module", None, False, False, EcucModuleDef),  # refinedModule
        ("supporteds", None, False, True, any (EcucConfiguration)),  # supporteds
    ]

    def __init__(self) -> None:
        """Initialize EcucModuleDef."""
        super().__init__()
        self.api_service_prefix: Optional[CIdentifier] = None
        self.containers: list[EcucContainerDef] = []
        self.post_build_variant: Optional[Boolean] = None
        self.refined_module: Optional[EcucModuleDef] = None
        self.supporteds: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucModuleDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucModuleDef":
        """Create EcucModuleDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucModuleDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucModuleDef since parent returns ARObject
        return cast("EcucModuleDef", obj)


class EcucModuleDefBuilder:
    """Builder for EcucModuleDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucModuleDef = EcucModuleDef()

    def build(self) -> EcucModuleDef:
        """Build and return EcucModuleDef object.

        Returns:
            EcucModuleDef instance
        """
        # TODO: Add validation
        return self._obj
