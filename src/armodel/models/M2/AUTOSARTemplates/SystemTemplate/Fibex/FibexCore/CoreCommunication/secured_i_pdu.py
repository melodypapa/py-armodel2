"""SecuredIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 367)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SecuredPduHeaderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class SecuredIPdu(IPdu):
    """AUTOSAR SecuredIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication: Optional[Any]
    dynamic: Optional[Boolean]
    freshness_props: Optional[Any]
    payload_ref: Optional[ARRef]
    secure: Optional[Any]
    use_as: Optional[Boolean]
    use_secured_pdu: Optional[SecuredPduHeaderEnum]
    def __init__(self) -> None:
        """Initialize SecuredIPdu."""
        super().__init__()
        self.authentication: Optional[Any] = None
        self.dynamic: Optional[Boolean] = None
        self.freshness_props: Optional[Any] = None
        self.payload_ref: Optional[ARRef] = None
        self.secure: Optional[Any] = None
        self.use_as: Optional[Boolean] = None
        self.use_secured_pdu: Optional[SecuredPduHeaderEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecuredIPdu":
        """Deserialize XML element to SecuredIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecuredIPdu object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse authentication
        child = ARObject._find_child_element(element, "AUTHENTICATION")
        if child is not None:
            authentication_value = child.text
            obj.authentication = authentication_value

        # Parse dynamic
        child = ARObject._find_child_element(element, "DYNAMIC")
        if child is not None:
            dynamic_value = child.text
            obj.dynamic = dynamic_value

        # Parse freshness_props
        child = ARObject._find_child_element(element, "FRESHNESS-PROPS")
        if child is not None:
            freshness_props_value = child.text
            obj.freshness_props = freshness_props_value

        # Parse payload_ref
        child = ARObject._find_child_element(element, "PAYLOAD")
        if child is not None:
            payload_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.payload_ref = payload_ref_value

        # Parse secure
        child = ARObject._find_child_element(element, "SECURE")
        if child is not None:
            secure_value = child.text
            obj.secure = secure_value

        # Parse use_as
        child = ARObject._find_child_element(element, "USE-AS")
        if child is not None:
            use_as_value = child.text
            obj.use_as = use_as_value

        # Parse use_secured_pdu
        child = ARObject._find_child_element(element, "USE-SECURED-PDU")
        if child is not None:
            use_secured_pdu_value = child.text
            obj.use_secured_pdu = use_secured_pdu_value

        return obj



class SecuredIPduBuilder:
    """Builder for SecuredIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecuredIPdu = SecuredIPdu()

    def build(self) -> SecuredIPdu:
        """Build and return SecuredIPdu object.

        Returns:
            SecuredIPdu instance
        """
        # TODO: Add validation
        return self._obj
