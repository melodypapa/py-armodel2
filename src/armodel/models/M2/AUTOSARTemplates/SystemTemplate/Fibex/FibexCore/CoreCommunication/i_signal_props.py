"""ISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 323)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ISignalProps(ARObject):
    """AUTOSAR ISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    handle_out_of_range: Optional[Any]
    def __init__(self) -> None:
        """Initialize ISignalProps."""
        super().__init__()
        self.handle_out_of_range: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalProps":
        """Deserialize XML element to ISignalProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse handle_out_of_range
        child = ARObject._find_child_element(element, "HANDLE-OUT-OF-RANGE")
        if child is not None:
            handle_out_of_range_value = child.text
            obj.handle_out_of_range = handle_out_of_range_value

        return obj



class ISignalPropsBuilder:
    """Builder for ISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalProps = ISignalProps()

    def build(self) -> ISignalProps:
        """Build and return ISignalProps object.

        Returns:
            ISignalProps instance
        """
        # TODO: Add validation
        return self._obj
