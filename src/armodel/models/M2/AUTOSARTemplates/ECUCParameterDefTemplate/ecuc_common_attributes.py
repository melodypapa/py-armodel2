"""EcucCommonAttributes AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_multiplicity_configuration_class import (
    EcucMultiplicityConfigurationClass,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_value_configuration_class import (
    EcucValueConfigurationClass,
)


class EcucCommonAttributes(EcucDefinitionElement):
    """AUTOSAR EcucCommonAttributes."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("multiplicities", None, False, True, EcucMultiplicityConfigurationClass),  # multiplicities
        ("origin", None, True, False, None),  # origin
        ("post_build_variant", None, True, False, None),  # postBuildVariant
        ("requires_index", None, True, False, None),  # requiresIndex
        ("value_configs", None, False, True, EcucValueConfigurationClass),  # valueConfigs
    ]

    def __init__(self) -> None:
        """Initialize EcucCommonAttributes."""
        super().__init__()
        self.multiplicities: list[EcucMultiplicityConfigurationClass] = []
        self.origin: Optional[String] = None
        self.post_build_variant: Optional[Boolean] = None
        self.requires_index: Optional[Boolean] = None
        self.value_configs: list[EcucValueConfigurationClass] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucCommonAttributes to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucCommonAttributes":
        """Create EcucCommonAttributes from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucCommonAttributes instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucCommonAttributes since parent returns ARObject
        return cast("EcucCommonAttributes", obj)


class EcucCommonAttributesBuilder:
    """Builder for EcucCommonAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucCommonAttributes = EcucCommonAttributes()

    def build(self) -> EcucCommonAttributes:
        """Build and return EcucCommonAttributes object.

        Returns:
            EcucCommonAttributes instance
        """
        # TODO: Add validation
        return self._obj
