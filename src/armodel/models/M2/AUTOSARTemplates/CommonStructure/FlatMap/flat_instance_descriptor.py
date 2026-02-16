"""FlatInstanceDescriptor AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.rte_plugin_props import (
    RtePluginProps,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class FlatInstanceDescriptor(Identifiable):
    """AUTOSAR FlatInstanceDescriptor."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecu_extract", None, False, False, AtpFeature),  # ecuExtract
        ("role", None, True, False, None),  # role
        ("rte_plugin_props", None, False, False, RtePluginProps),  # rtePluginProps
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
        ("upstream", None, False, False, AtpFeature),  # upstream
    ]

    def __init__(self) -> None:
        """Initialize FlatInstanceDescriptor."""
        super().__init__()
        self.ecu_extract: Optional[AtpFeature] = None
        self.role: Optional[Identifier] = None
        self.rte_plugin_props: Optional[RtePluginProps] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.upstream: Optional[AtpFeature] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlatInstanceDescriptor to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlatInstanceDescriptor":
        """Create FlatInstanceDescriptor from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlatInstanceDescriptor instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlatInstanceDescriptor since parent returns ARObject
        return cast("FlatInstanceDescriptor", obj)


class FlatInstanceDescriptorBuilder:
    """Builder for FlatInstanceDescriptor."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlatInstanceDescriptor = FlatInstanceDescriptor()

    def build(self) -> FlatInstanceDescriptor:
        """Build and return FlatInstanceDescriptor object.

        Returns:
            FlatInstanceDescriptor instance
        """
        # TODO: Add validation
        return self._obj
