"""DataPrototypeInClientServerInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 788)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef.data_prototype_in_port_interface_instance_ref import (
    DataPrototypeInPortInterfaceInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_interface import (
    ClientServerInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInClientServerInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """AUTOSAR DataPrototypeInClientServerInterfaceInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[ClientServerInterface]
    context_datas: list[Any]
    root_data_prototype_in_cs_ref: Optional[ARRef]
    target_data_prototype_in_cs_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataPrototypeInClientServerInterfaceInstanceRef."""
        super().__init__()
        self.base: Optional[ClientServerInterface] = None
        self.context_datas: list[Any] = []
        self.root_data_prototype_in_cs_ref: Optional[ARRef] = None
        self.target_data_prototype_in_cs_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """Deserialize XML element to DataPrototypeInClientServerInterfaceInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInClientServerInterfaceInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "ClientServerInterface")
            obj.base = base_value

        # Parse context_datas (list)
        obj.context_datas = []
        for child in ARObject._find_all_child_elements(element, "CONTEXT-DATAS"):
            context_datas_value = child.text
            obj.context_datas.append(context_datas_value)

        # Parse root_data_prototype_in_cs_ref
        child = ARObject._find_child_element(element, "ROOT-DATA-PROTOTYPE-IN-CS")
        if child is not None:
            root_data_prototype_in_cs_ref_value = ARObject._deserialize_by_tag(child, "AutosarDataPrototype")
            obj.root_data_prototype_in_cs_ref = root_data_prototype_in_cs_ref_value

        # Parse target_data_prototype_in_cs_ref
        child = ARObject._find_child_element(element, "TARGET-DATA-PROTOTYPE-IN-CS")
        if child is not None:
            target_data_prototype_in_cs_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.target_data_prototype_in_cs_ref = target_data_prototype_in_cs_ref_value

        return obj



class DataPrototypeInClientServerInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInClientServerInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInClientServerInterfaceInstanceRef = DataPrototypeInClientServerInterfaceInstanceRef()

    def build(self) -> DataPrototypeInClientServerInterfaceInstanceRef:
        """Build and return DataPrototypeInClientServerInterfaceInstanceRef object.

        Returns:
            DataPrototypeInClientServerInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
