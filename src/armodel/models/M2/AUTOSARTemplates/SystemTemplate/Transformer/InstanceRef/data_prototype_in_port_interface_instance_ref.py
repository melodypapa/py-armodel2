"""DataPrototypeInPortInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1009)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from abc import ABC, abstractmethod


class DataPrototypeInPortInterfaceInstanceRef(ARObject, ABC):
    """AUTOSAR DataPrototypeInPortInterfaceInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    abstract_base: Optional[PortInterface]
    context_datas: list[Any]
    root_data_ref: Optional[ARRef]
    target_data_ref: ARRef
    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceInstanceRef."""
        super().__init__()
        self.abstract_base: Optional[PortInterface] = None
        self.context_datas: list[Any] = []
        self.root_data_ref: Optional[ARRef] = None
        self.target_data_ref: ARRef = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInPortInterfaceInstanceRef":
        """Deserialize XML element to DataPrototypeInPortInterfaceInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInPortInterfaceInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse abstract_base
        child = ARObject._find_child_element(element, "ABSTRACT-BASE")
        if child is not None:
            abstract_base_value = ARObject._deserialize_by_tag(child, "PortInterface")
            obj.abstract_base = abstract_base_value

        # Parse context_datas (list)
        obj.context_datas = []
        for child in ARObject._find_all_child_elements(element, "CONTEXT-DATAS"):
            context_datas_value = child.text
            obj.context_datas.append(context_datas_value)

        # Parse root_data_ref
        child = ARObject._find_child_element(element, "ROOT-DATA")
        if child is not None:
            root_data_ref_value = ARObject._deserialize_by_tag(child, "AutosarDataPrototype")
            obj.root_data_ref = root_data_ref_value

        # Parse target_data_ref
        child = ARObject._find_child_element(element, "TARGET-DATA")
        if child is not None:
            target_data_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.target_data_ref = target_data_ref_value

        return obj



class DataPrototypeInPortInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInPortInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInPortInterfaceInstanceRef = DataPrototypeInPortInterfaceInstanceRef()

    def build(self) -> DataPrototypeInPortInterfaceInstanceRef:
        """Build and return DataPrototypeInPortInterfaceInstanceRef object.

        Returns:
            DataPrototypeInPortInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
