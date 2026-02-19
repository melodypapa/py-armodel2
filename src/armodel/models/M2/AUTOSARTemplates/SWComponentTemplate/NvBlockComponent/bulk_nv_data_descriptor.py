"""BulkNvDataDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 692)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_data_mapping import (
    NvBlockDataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class BulkNvDataDescriptor(Identifiable):
    """AUTOSAR BulkNvDataDescriptor."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bulk_nv_block_ref: Optional[ARRef]
    nv_block_data_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BulkNvDataDescriptor."""
        super().__init__()
        self.bulk_nv_block_ref: Optional[ARRef] = None
        self.nv_block_data_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BulkNvDataDescriptor":
        """Deserialize XML element to BulkNvDataDescriptor object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BulkNvDataDescriptor object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bulk_nv_block_ref
        child = ARObject._find_child_element(element, "BULK-NV-BLOCK")
        if child is not None:
            bulk_nv_block_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.bulk_nv_block_ref = bulk_nv_block_ref_value

        # Parse nv_block_data_refs (list)
        obj.nv_block_data_refs = []
        for child in ARObject._find_all_child_elements(element, "NV-BLOCK-DATAS"):
            nv_block_data_refs_value = ARObject._deserialize_by_tag(child, "NvBlockDataMapping")
            obj.nv_block_data_refs.append(nv_block_data_refs_value)

        return obj



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
