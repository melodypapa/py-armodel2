"""SecuredIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 367)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class SecuredIPdu(IPdu):
    """AUTOSAR SecuredIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "authentication": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SecureCommunication),
        ),  # authentication
        "dynamic": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dynamic
        "freshness_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SecureCommunication),
        ),  # freshnessProps
        "payload": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # payload
        "secure": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SecureCommunication),
        ),  # secure
        "use_as": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # useAs
        "use_secured_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SecuredPduHeaderEnum,
        ),  # useSecuredPdu
    }

    def __init__(self) -> None:
        """Initialize SecuredIPdu."""
        super().__init__()
        self.authentication: Optional[Any] = None
        self.dynamic: Optional[Boolean] = None
        self.freshness_props: Optional[Any] = None
        self.payload: Optional[PduTriggering] = None
        self.secure: Optional[Any] = None
        self.use_as: Optional[Boolean] = None
        self.use_secured_pdu: Optional[SecuredPduHeaderEnum] = None


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
