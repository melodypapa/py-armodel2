"""MsrQueryArg AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class MsrQueryArg(ARObject):
    """AUTOSAR MsrQueryArg."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arg: String
    si: NameToken
    def __init__(self) -> None:
        """Initialize MsrQueryArg."""
        super().__init__()
        self.arg: String = None
        self.si: NameToken = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryArg":
        """Deserialize XML element to MsrQueryArg object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryArg object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse arg
        child = ARObject._find_child_element(element, "ARG")
        if child is not None:
            arg_value = child.text
            obj.arg = arg_value

        # Parse si
        child = ARObject._find_child_element(element, "SI")
        if child is not None:
            si_value = child.text
            obj.si = si_value

        return obj



class MsrQueryArgBuilder:
    """Builder for MsrQueryArg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryArg = MsrQueryArg()

    def build(self) -> MsrQueryArg:
        """Build and return MsrQueryArg object.

        Returns:
            MsrQueryArg instance
        """
        # TODO: Add validation
        return self._obj
