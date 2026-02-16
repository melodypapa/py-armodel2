"""EcucModuleConfigurationValues AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)


class EcucModuleConfigurationValues(ARElement):
    """AUTOSAR EcucModuleConfigurationValues."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("containers", None, False, True, EcucContainerValue),  # containers
        ("definition", None, False, False, EcucModuleDef),  # definition
        ("ecuc_def_edition", None, True, False, None),  # ecucDefEdition
        ("implementation", None, False, False, any (EcucConfiguration)),  # implementation
        ("module", None, False, False, BswImplementation),  # module
        ("post_build_variant", None, True, False, None),  # postBuildVariant
    ]

    def __init__(self) -> None:
        """Initialize EcucModuleConfigurationValues."""
        super().__init__()
        self.containers: list[EcucContainerValue] = []
        self.definition: Optional[EcucModuleDef] = None
        self.ecuc_def_edition: Optional[RevisionLabelString] = None
        self.implementation: Optional[Any] = None
        self.module: Optional[BswImplementation] = None
        self.post_build_variant: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucModuleConfigurationValues to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucModuleConfigurationValues":
        """Create EcucModuleConfigurationValues from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucModuleConfigurationValues instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucModuleConfigurationValues since parent returns ARObject
        return cast("EcucModuleConfigurationValues", obj)


class EcucModuleConfigurationValuesBuilder:
    """Builder for EcucModuleConfigurationValues."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucModuleConfigurationValues = EcucModuleConfigurationValues()

    def build(self) -> EcucModuleConfigurationValues:
        """Build and return EcucModuleConfigurationValues object.

        Returns:
            EcucModuleConfigurationValues instance
        """
        # TODO: Add validation
        return self._obj
