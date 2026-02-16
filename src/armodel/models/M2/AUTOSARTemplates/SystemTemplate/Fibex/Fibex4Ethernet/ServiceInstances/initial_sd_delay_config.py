"""InitialSdDelayConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class InitialSdDelayConfig(ARObject):
    """AUTOSAR InitialSdDelayConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("initial_delay_max", None, True, False, None),  # initialDelayMax
        ("initial_delay_min", None, True, False, None),  # initialDelayMin
        ("initial", None, True, False, None),  # initial
    ]

    def __init__(self) -> None:
        """Initialize InitialSdDelayConfig."""
        super().__init__()
        self.initial_delay_max: Optional[TimeValue] = None
        self.initial_delay_min: Optional[TimeValue] = None
        self.initial: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InitialSdDelayConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InitialSdDelayConfig":
        """Create InitialSdDelayConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InitialSdDelayConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InitialSdDelayConfig since parent returns ARObject
        return cast("InitialSdDelayConfig", obj)


class InitialSdDelayConfigBuilder:
    """Builder for InitialSdDelayConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InitialSdDelayConfig = InitialSdDelayConfig()

    def build(self) -> InitialSdDelayConfig:
        """Build and return InitialSdDelayConfig object.

        Returns:
            InitialSdDelayConfig instance
        """
        # TODO: Add validation
        return self._obj
