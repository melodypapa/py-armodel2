"""LinSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_error_response import (
    LinErrorResponse,
)


class LinSlave(ARObject):
    """AUTOSAR LinSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assign_nad: Optional[Boolean]
    configured_nad: Optional[Integer]
    function_id: Optional[PositiveInteger]
    initial_nad: Optional[Integer]
    lin_error_response: Optional[LinErrorResponse]
    nas_timeout: Optional[TimeValue]
    supplier_id: Optional[PositiveInteger]
    variant_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize LinSlave."""
        super().__init__()
        self.assign_nad: Optional[Boolean] = None
        self.configured_nad: Optional[Integer] = None
        self.function_id: Optional[PositiveInteger] = None
        self.initial_nad: Optional[Integer] = None
        self.lin_error_response: Optional[LinErrorResponse] = None
        self.nas_timeout: Optional[TimeValue] = None
        self.supplier_id: Optional[PositiveInteger] = None
        self.variant_id: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinSlave":
        """Deserialize XML element to LinSlave object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinSlave object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse assign_nad
        child = ARObject._find_child_element(element, "ASSIGN-NAD")
        if child is not None:
            assign_nad_value = child.text
            obj.assign_nad = assign_nad_value

        # Parse configured_nad
        child = ARObject._find_child_element(element, "CONFIGURED-NAD")
        if child is not None:
            configured_nad_value = child.text
            obj.configured_nad = configured_nad_value

        # Parse function_id
        child = ARObject._find_child_element(element, "FUNCTION-ID")
        if child is not None:
            function_id_value = child.text
            obj.function_id = function_id_value

        # Parse initial_nad
        child = ARObject._find_child_element(element, "INITIAL-NAD")
        if child is not None:
            initial_nad_value = child.text
            obj.initial_nad = initial_nad_value

        # Parse lin_error_response
        child = ARObject._find_child_element(element, "LIN-ERROR-RESPONSE")
        if child is not None:
            lin_error_response_value = ARObject._deserialize_by_tag(child, "LinErrorResponse")
            obj.lin_error_response = lin_error_response_value

        # Parse nas_timeout
        child = ARObject._find_child_element(element, "NAS-TIMEOUT")
        if child is not None:
            nas_timeout_value = child.text
            obj.nas_timeout = nas_timeout_value

        # Parse supplier_id
        child = ARObject._find_child_element(element, "SUPPLIER-ID")
        if child is not None:
            supplier_id_value = child.text
            obj.supplier_id = supplier_id_value

        # Parse variant_id
        child = ARObject._find_child_element(element, "VARIANT-ID")
        if child is not None:
            variant_id_value = child.text
            obj.variant_id = variant_id_value

        return obj



class LinSlaveBuilder:
    """Builder for LinSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinSlave = LinSlave()

    def build(self) -> LinSlave:
        """Build and return LinSlave object.

        Returns:
            LinSlave instance
        """
        # TODO: Add validation
        return self._obj
