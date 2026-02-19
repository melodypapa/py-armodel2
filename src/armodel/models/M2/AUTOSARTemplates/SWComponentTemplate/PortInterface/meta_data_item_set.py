"""MetaDataItemSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 99)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2037)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.meta_data_item import (
    MetaDataItem,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class MetaDataItemSet(ARObject):
    """AUTOSAR MetaDataItemSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element_refs: list[ARRef]
    meta_data_items: list[MetaDataItem]
    def __init__(self) -> None:
        """Initialize MetaDataItemSet."""
        super().__init__()
        self.data_element_refs: list[ARRef] = []
        self.meta_data_items: list[MetaDataItem] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MetaDataItemSet":
        """Deserialize XML element to MetaDataItemSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MetaDataItemSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_element_refs (list)
        obj.data_element_refs = []
        for child in ARObject._find_all_child_elements(element, "DATA-ELEMENTS"):
            data_element_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_element_refs.append(data_element_refs_value)

        # Parse meta_data_items (list)
        obj.meta_data_items = []
        for child in ARObject._find_all_child_elements(element, "META-DATA-ITEMS"):
            meta_data_items_value = ARObject._deserialize_by_tag(child, "MetaDataItem")
            obj.meta_data_items.append(meta_data_items_value)

        return obj



class MetaDataItemSetBuilder:
    """Builder for MetaDataItemSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MetaDataItemSet = MetaDataItemSet()

    def build(self) -> MetaDataItemSet:
        """Build and return MetaDataItemSet object.

        Returns:
            MetaDataItemSet instance
        """
        # TODO: Add validation
        return self._obj
