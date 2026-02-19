"""DataPrototypeInPortInterfaceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 787)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
    DataPrototypeReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInPortInterfaceRef(DataPrototypeReference):
    """AUTOSAR DataPrototypeInPortInterfaceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_prototype_in_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceRef."""
        super().__init__()
        self.data_prototype_in_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInPortInterfaceRef":
        """Deserialize XML element to DataPrototypeInPortInterfaceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInPortInterfaceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_prototype_in_ref
        child = ARObject._find_child_element(element, "DATA-PROTOTYPE-IN")
        if child is not None:
            data_prototype_in_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.data_prototype_in_ref = data_prototype_in_ref_value

        return obj



class DataPrototypeInPortInterfaceRefBuilder:
    """Builder for DataPrototypeInPortInterfaceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInPortInterfaceRef = DataPrototypeInPortInterfaceRef()

    def build(self) -> DataPrototypeInPortInterfaceRef:
        """Build and return DataPrototypeInPortInterfaceRef object.

        Returns:
            DataPrototypeInPortInterfaceRef instance
        """
        # TODO: Add validation
        return self._obj
