"""SwcToSwcSignal AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SwcToSwcSignal(ARObject):
    """AUTOSAR SwcToSwcSignal."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize SwcToSwcSignal."""
        super().__init__()
        self.data_element_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToSwcSignal":
        """Deserialize XML element to SwcToSwcSignal object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToSwcSignal object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_element_refs (list)
        obj.data_element_refs = []
        for child in ARObject._find_all_child_elements(element, "DATA-ELEMENTS"):
            data_element_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_element_refs.append(data_element_refs_value)

        return obj



class SwcToSwcSignalBuilder:
    """Builder for SwcToSwcSignal."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToSwcSignal = SwcToSwcSignal()

    def build(self) -> SwcToSwcSignal:
        """Build and return SwcToSwcSignal object.

        Returns:
            SwcToSwcSignal instance
        """
        # TODO: Add validation
        return self._obj
