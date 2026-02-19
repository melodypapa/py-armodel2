"""ParameterInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 41)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)


class ParameterInterface(DataInterface):
    """AUTOSAR ParameterInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    parameter_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ParameterInterface."""
        super().__init__()
        self.parameter_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterInterface":
        """Deserialize XML element to ParameterInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterInterface object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse parameter_refs (list)
        obj.parameter_refs = []
        for child in ARObject._find_all_child_elements(element, "PARAMETERS"):
            parameter_refs_value = ARObject._deserialize_by_tag(child, "ParameterDataPrototype")
            obj.parameter_refs.append(parameter_refs_value)

        return obj



class ParameterInterfaceBuilder:
    """Builder for ParameterInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterInterface = ParameterInterface()

    def build(self) -> ParameterInterface:
        """Build and return ParameterInterface object.

        Returns:
            ParameterInterface instance
        """
        # TODO: Add validation
        return self._obj
