"""BulkNvDataDescriptor AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_data_mapping import (
    NvBlockDataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class BulkNvDataDescriptor(Identifiable):
    """AUTOSAR BulkNvDataDescriptor."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bulk_nv_block", None, False, False, VariableDataPrototype),  # bulkNvBlock
        ("nv_block_datas", None, False, True, NvBlockDataMapping),  # nvBlockDatas
    ]

    def __init__(self) -> None:
        """Initialize BulkNvDataDescriptor."""
        super().__init__()
        self.bulk_nv_block: Optional[VariableDataPrototype] = None
        self.nv_block_datas: list[NvBlockDataMapping] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BulkNvDataDescriptor to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BulkNvDataDescriptor":
        """Create BulkNvDataDescriptor from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BulkNvDataDescriptor instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BulkNvDataDescriptor since parent returns ARObject
        return cast("BulkNvDataDescriptor", obj)


class BulkNvDataDescriptorBuilder:
    """Builder for BulkNvDataDescriptor."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BulkNvDataDescriptor = BulkNvDataDescriptor()

    def build(self) -> BulkNvDataDescriptor:
        """Build and return BulkNvDataDescriptor object.

        Returns:
            BulkNvDataDescriptor instance
        """
        # TODO: Add validation
        return self._obj
